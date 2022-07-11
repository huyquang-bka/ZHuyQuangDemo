from PyQt5 import QtCore
import time
import cv2
from Yolov5.detect_yolov5 import Detection
from Polygon.Polygon import plate_polygon
import string
import config


class ThreadDigit(QtCore.QThread):

    def __init__(self, queue_plate, queue_digit):
        super().__init__()
        self.__thread_active = False

        # queue
        self.queue_plate = queue_plate
        self.queue_digit = queue_digit

        # tracking
        self.digit_detection = Detection()
        self.setup_digit_detection()

        self.allow_lp = string.ascii_uppercase + string.digits

        self.middle_height = 400

    def setup_digit_detection(self):
        weights = "Weight/digit.pt"
        classes = None
        conf = 0.5
        imgsz = 640
        device = config.device
        self.digit_detection.setup_model(weights, classes, conf, imgsz, device)

    def is_square_lp(self, image):
        return image.shape[1] / image.shape[0] <= 2

    def clean_lp(self, bboxes):
        lp_text = ""
        for i in range(len(bboxes)):
            x1, y1, x2, y2, cls, conf = bboxes[i]
            center_x, center_y = (x1 + x2) / 2, (y1 + y2) / 2
            if cls.upper() not in self.allow_lp:
                continue
            digit = cls.upper()
            for ii in range(len(bboxes)):
                if ii == i:
                    continue
                x1_, y1_, x2_, y2_, cls_, conf_ = bboxes[ii]
                if x1_ < center_x < x2_ and y1_ < center_y < y2_:
                    if float(conf) > float(conf_):
                        digit = cls.upper()
                    else:
                        digit = ""
            lp_text += digit
        return lp_text

    def process_square_lp(self, bboxes):
        line_1 = []
        line_2 = []
        all_y = [box[1] for box in bboxes]
        if len(all_y) == 0:
            return []
        average_y = sum(all_y) / len(all_y)
        for bbox in bboxes:
            if bbox[1] < average_y:
                line_1.append(bbox)
            else:
                line_2.append(bbox)
        line_1 = sorted(line_1, key=lambda x: x[0])
        line_2 = sorted(line_2, key=lambda x: x[0])
        return line_1 + line_2

    def most_frequent(self, ls):
        try:
            return max(set(ls), key=ls.count)
        except:
            return ""

    def run(self):
        self.__thread_active = True
        print('Starting Plate Thread...')
        count = 0
        digit_dict = {}
        while self.__thread_active:
            if self.queue_plate.qsize() > 0:
                frame, id_dict = self.queue_plate.get()
                result_dict = {}
                for id, bbox in id_dict.items():
                    count += 1
                    box, plate_box = bbox
                    x1, y1, x2, y2 = box
                    if not plate_box:
                        if (y1 + y2) // 2 > self.middle_height:
                            list_key = list(digit_dict.keys())
                            if id in list_key:
                                digit_dict[id].append(" ")
                                lp_text = self.most_frequent(digit_dict[id])
                                result_dict[id] = lp_text
                                del digit_dict[id]
                            if self.queue_digit.qsize() < 1 and result_dict:
                                # print("Digit: ", digit_dict)
                                self.queue_digit.put(result_dict)
                        continue

                    try:
                        digit_dict[id]
                    except:
                        digit_dict[id] = []

                    x1_, y1_, x2_, y2_, cls_, conf_ = plate_box
                    crop = frame[y1:y2, x1:x2]
                    lp_crop = crop[y1_:y2_, x1_:x2_]
                    # cv2.imwrite(f"Crop/{id}_{count}.jpg", lp_crop)
                    digit_list = self.digit_detection.detect(lp_crop)
                    digit_list = sorted(digit_list, key=lambda x: x[0])
                    is_square = self.is_square_lp(lp_crop)
                    if is_square:
                        digit_list = self.process_square_lp(digit_list)
                    lp_text = self.clean_lp(digit_list)
                    if len(lp_text) < 7:
                        continue
                    digit_dict[id].append(lp_text)
            QtCore.QThread.msleep(1)

    def stop(self):
        print('Stopping Plate Thread')
        self.__thread_active = False
