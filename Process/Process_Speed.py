from PyQt5 import QtCore
import time
import cv2
from Yolov5.detect_yolov5 import Detection
from Polygon.Polygon import plate_polygon, detect_polygon


class ThreadSpeed(QtCore.QThread):

    def __init__(self, queue_tracking_for_speed, queue_speed):
        super().__init__()
        self.__thread_active = False

        # queue
        self.queue_tracking_for_speed = queue_tracking_for_speed
        self.queue_speed = queue_speed

        # distance
        self.distance = 15

    def is_in_detect_zone(self, box):
        x1, y1, x2, y2 = box
        return cv2.pointPolygonTest(detect_polygon, ((x1 + x2) // 2, y2), False) > 0

    def run(self):
        self.__thread_active = True
        print('Starting Speed Thread...')
        speed_dict = {}
        real_speed_dict = {}
        while self.__thread_active:
            n = len(speed_dict)
            n_ = len(real_speed_dict)
            if n > 20:
                for i in list(sorted(speed_dict.keys()))[:n - 20]:
                    del speed_dict[i]
            if self.queue_tracking_for_speed.qsize() > 0:
                frame, id_dict = self.queue_tracking_for_speed.get()
                for id, bbox in id_dict.items():
                    box = bbox[:4]
                    x1, y1, x2, y2, cls = bbox
                    if int(cls) not in [2, 7]:
                        continue
                    is_in_detect_zone = self.is_in_detect_zone(box)
                    center_y_plate = (detect_polygon[0][0][1] + detect_polygon[1][0][1]) / 2
                    if is_in_detect_zone and id not in speed_dict.keys() and y2 < center_y_plate:
                        speed_dict[id] = [1, time.time()]
                    elif not is_in_detect_zone and y2 > center_y_plate and id in speed_dict.keys():
                        f = speed_dict[id][1]
                        real_speed_dict[id] = int(self.distance / (time.time() - f) * 3.6)
                        del speed_dict[id]

                if self.queue_speed.qsize() < 1 and real_speed_dict:
                    # print("Speed: ", real_speed_dict)
                    self.queue_speed.put(real_speed_dict)
            QtCore.QThread.msleep(1)

    def stop(self):
        print('Stopping Speed Thread')
        self.__thread_active = False
