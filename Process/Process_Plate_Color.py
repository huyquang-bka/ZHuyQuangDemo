from PyQt5 import QtCore
import time
import cv2
import numpy as np

from PyQt5 import QtCore
import time
import cv2
from Yolov5.detect_yolov5 import Detection
from Polygon.Polygon import plate_polygon, detect_polygon
import config


class ThreadPlateColor(QtCore.QThread):

    def __init__(self, queue_plate, queue_plate_color):
        super().__init__()
        self.__thread_active = False

        # queue
        self.queue_plate = queue_plate
        self.queue_plate_color = queue_plate_color

        self.middle_height = 400

        # tracking
        self.color_plate_detection = Detection()
        self.setup_color_plate_detection()

        self.middle_height = 400

    def setup_color_plate_detection(self):
        weights = "Weight/color_plate.pt"
        classes = None
        conf = 0.3
        imgsz = 640
        device = config.device
        self.color_plate_detection.setup_model(weights, classes, conf, imgsz, device)

    def is_in_plate_zone(self, box):
        x1, y1, x2, y2 = box
        return cv2.pointPolygonTest(plate_polygon, ((x1 + x2) // 2, y2), False) > 0

    def is_in_detect_zone(self, box):
        x1, y1, x2, y2 = box
        return cv2.pointPolygonTest(detect_polygon, ((x1 + x2) // 2, y2), False) > 0

    def most_frequent(self, ls):
        try:
            return max(set(ls), key=ls.count)
        except:
            return ""

    def run(self):
        self.__thread_active = True
        print('Starting Color Plate Thread...')
        count = 0
        color_plate_dict = {}
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
                            list_key = list(color_plate_dict.keys())
                            if id in list_key:
                                color_plate_dict[id].append(" ")
                                lp_text = self.most_frequent(color_plate_dict[id])
                                result_dict[id] = lp_text
                                del color_plate_dict[id]
                            if self.queue_plate_color.qsize() < 1 and result_dict:
                                # print("Digit: ", color_plate_dict)
                                self.queue_plate_color.put(result_dict)
                        continue

                    try:
                        color_plate_dict[id]
                    except:
                        color_plate_dict[id] = []

                    x1_, y1_, x2_, y2_, cls_, conf_ = plate_box
                    crop = frame[y1:y2, x1:x2]
                    lp_crop = crop[y1_:y2_, x1_:x2_]
                    # cv2.imwrite(f"Crop/{id}_{count}.jpg", lp_crop)
                    color_plate_list = self.color_plate_detection.detect(lp_crop)
                    if color_plate_list:
                        color_plate = color_plate_list[0][4]
                        color_plate_dict[id].append(color_plate)
            QtCore.QThread.msleep(1)

    def stop(self):
        print('Stopping Brand Thread')
        self.__thread_active = False
