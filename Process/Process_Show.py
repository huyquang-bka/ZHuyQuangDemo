from PyQt5 import QtCore
import time
import cv2
from Polygon.Polygon import detect_polygon, plate_polygon
from datetime import datetime


class ThreadShow(QtCore.QThread):
    sig_info_vehicle = QtCore.pyqtSignal(dict)

    def __init__(self, queue_tracking, queue_output):
        super().__init__()
        self.__thread_active = False

        # queue
        self.queue_tracking = queue_tracking
        self.queue_output = queue_output

        # crop
        self.crop_dict = {}

        # signal
        self.summary_dict = {}

    def slot_summary(self, summary_dict):
        self.summary_dict = summary_dict
        # print(summary_dict)

    def draw(self, frame, id_dict):
        frame_copy = frame.copy()
        for k, v in id_dict.items():
            x1, y1, x2, y2, category = v
            if not self.is_in_detect_zone(v[:4]):
                continue
            try:
                self.crop_dict[k]
            except:
                self.crop_dict[k] = None
            if self.is_in_plate_zone(v[:4]) and self.crop_dict[k] is None:
                self.crop_dict[k] = frame_copy[y1:y2, x1:x2]
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, str(k), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    def is_in_plate_zone(self, box):
        x1, y1, x2, y2 = box
        return cv2.pointPolygonTest(plate_polygon, ((x1 + x2) // 2, y2), False) > 0

    def is_in_detect_zone(self, box):
        x1, y1, x2, y2 = box
        return cv2.pointPolygonTest(detect_polygon, ((x1 + x2) // 2, y2), False) > 0

    def run(self):
        self.__thread_active = True
        print('Starting Tracking Thread...')
        while self.__thread_active:
            if self.queue_tracking.qsize() > 0:
                frame, id_dict = self.queue_tracking.get()
                self.draw(frame, id_dict)
                if self.queue_output.qsize() < 1:
                    self.queue_output.put(frame)
                for k, v in id_dict.items():
                    if k in list(self.summary_dict.keys()):
                        color, brand, plate, speed, plate_color = self.summary_dict[k]
                        if plate and speed:
                            try:
                                crop = self.crop_dict[k]
                                del self.crop_dict[k]
                            except:
                                crop = None
                            date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            emit_dict = {"color": color, "brand": brand, "plate": plate, "speed": str(speed),
                                         "crop": crop, "date_time": date_time, "plate_color": plate_color, "id": k}
                            self.sig_info_vehicle.emit(emit_dict)
                            del self.summary_dict[k]
            QtCore.QThread.msleep(1)

    def stop(self):
        print('Stopping Capture Thread')
        self.__thread_active = False
