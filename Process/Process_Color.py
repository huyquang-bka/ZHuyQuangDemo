from PyQt5 import QtCore
import time
import cv2
from Color.classify import Classifier
from Polygon.Polygon import plate_polygon, detect_polygon


class ThreadColor(QtCore.QThread):

    def __init__(self, queue_tracking_for_color, queue_color):
        super().__init__()
        self.__thread_active = False

        # queue
        self.queue_tracking_for_color = queue_tracking_for_color
        self.queue_color = queue_color

        # tracking
        self.color_detection = Classifier("Color/color.mnn", "Color/labels-color.txt")

        self.middle_height = 400

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
        print('Starting Color Thread...')
        color_dict = {}
        while self.__thread_active:
            result_dict = {}
            if self.queue_tracking_for_color.qsize() > 0:
                frame, id_dict = self.queue_tracking_for_color.get()
                for id, bbox in id_dict.items():
                    box = bbox[:4]
                    x1, y1, x2, y2, cls = bbox
                    if int(cls) not in [2, 7] or not self.is_in_detect_zone(box):
                        continue
                    crop = frame[y1:y2, x1:x2]
                    if self.is_in_plate_zone(box):
                        try:
                            color_dict[id]
                        except:
                            color_dict[id] = []
                        color, conf = self.color_detection.predict(crop)
                        color_dict[id].append(color)
                    elif (y1 + y2) / 2 > self.middle_height:
                        list_key = list(color_dict.keys())
                        if id in list_key:
                            color_dict[id].append(" ")
                            color = self.most_frequent(color_dict[id])
                            result_dict[id] = color
                            del color_dict[id]
                if self.queue_color.qsize() < 1 and result_dict:
                    # print("Color: ", color_dict)
                    self.queue_color.put(result_dict)
            QtCore.QThread.msleep(1)

    def stop(self):
        print('Stopping Color Thread')
        self.__thread_active = False
