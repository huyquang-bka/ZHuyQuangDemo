from PyQt5 import QtCore
import time
import cv2
from Yolov5.detect_yolov5 import Detection
from Polygon.Polygon import plate_polygon, detect_polygon
import config


class ThreadBrand(QtCore.QThread):

    def __init__(self, queue_tracking_for_brand, queue_brand):
        super().__init__()
        self.__thread_active = False

        # queue
        self.queue_tracking_for_brand = queue_tracking_for_brand
        self.queue_brand = queue_brand

        # tracking
        self.brand_detection = Detection()
        self.setup_brand_detection()

        self.middle_height = 400

    def setup_brand_detection(self):
        weights = "Weight/brand.pt"
        classes = None
        conf = 0.5
        imgsz = 640
        device = config.device
        self.brand_detection.setup_model(weights, classes, conf, imgsz, device)

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
        print('Starting Brand Thread...')
        brand_dict = {}
        while self.__thread_active:
            result_dict = {}
            if self.queue_tracking_for_brand.qsize() > 0:
                frame, id_dict = self.queue_tracking_for_brand.get()
                for id, bbox in id_dict.items():
                    box = bbox[:4]
                    x1, y1, x2, y2, cls = bbox
                    if int(cls) not in [2, 7] or not self.is_in_detect_zone(box):
                        continue
                    crop = frame[y1:y2, x1:x2]
                    if self.is_in_plate_zone(box):
                        try:
                            brand_dict[id]
                        except:
                            brand_dict[id] = []
                        brand_list = self.brand_detection.detect(crop)
                        if brand_list:
                            brand = brand_list[0][4].split("____")[1]
                            brand_dict[id].append(brand)
                    else:
                        if (y1 + y2) / 2 > self.middle_height:
                            list_key = list(brand_dict.keys())
                            if id in list_key:
                                brand_dict[id].append(" ")
                                brand = self.most_frequent(brand_dict[id])
                                result_dict[id] = brand
                                del brand_dict[id]
                if self.queue_brand.qsize() < 1 and result_dict:
                    self.queue_brand.put(result_dict)
            QtCore.QThread.msleep(1)

    def stop(self):
        print('Stopping Brand Thread')
        self.__thread_active = False
