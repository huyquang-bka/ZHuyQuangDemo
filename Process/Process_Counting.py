from PyQt5 import QtCore
from Polygon.Polygon import detect_polygon, plate_polygon, points_detect
import cv2


class ThreadCounting(QtCore.QThread):
    sig_count_motor = QtCore.pyqtSignal(int)
    sig_count_car = QtCore.pyqtSignal(int)
    sig_video_car = QtCore.pyqtSignal(list)

    def __init__(self, queue_tracking_for_count):
        super().__init__()
        self.__thread_active = False

        # queue
        self.queue_tracking_for_count = queue_tracking_for_count

        self.max_height = 900

        self.num_frame = 30
        self.w = 640
        self.h = 480

    def is_in_detect_zone(self, box):
        x1, y1, x2, y2 = box
        return cv2.pointPolygonTest(detect_polygon, ((x1 + x2) // 2, y2), False) > 0

    def is_in_plate_zone(self, box):
        x1, y1, x2, y2 = box
        return cv2.pointPolygonTest(plate_polygon, ((x1 + x2) // 2, y2), False) > 0

    def run(self):
        self.__thread_active = True
        print('Starting Tracking Thread...')
        list_id = []
        id_dict = {}
        while self.__thread_active:
            if self.queue_tracking_for_count.qsize() > 0:
                frame, tracking_dict = self.queue_tracking_for_count.get()
                # cv2.polylines(frame, [points_detect], True, (0, 255, 0), 2)
                for id, value in tracking_dict.items():
                    x1, y1, x2, y2, category = value[:5]
                    if not self.is_in_detect_zone([x1, y1, x2, y2]):
                        continue
                    if int(category) == 3:
                        if id in list_id:
                            continue
                        self.sig_count_motor.emit(0)
                    else:
                        if not (id in list_id):
                            self.sig_count_car.emit(0)
                        if not self.is_in_plate_zone([x1, y1, x2, y2]) and y2 > self.max_height:
                            if id_dict:
                                if len(id_dict[id]) >= 30:
                                    self.sig_video_car.emit([id, id_dict[id][::int(len(id_dict[id]) / self.num_frame)]])
                                else:
                                    self.sig_video_car.emit([id, id_dict[id]])
                                del id_dict[id]
                            continue
                        try:
                            id_dict[id]
                        except:
                            id_dict[id] = []
                        id_dict[id].append(cv2.resize(frame, (self.w, self.h)))

                    list_id.append(id)
            QtCore.QThread.msleep(1)

    def stop(self):
        print('Stopping Capture Thread')
        self.__thread_active = False
