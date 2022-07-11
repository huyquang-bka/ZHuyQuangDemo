from PyQt5 import QtCore
import time
import cv2
from Yolov5.detect_yolov5 import Tracking
import config


class ThreadTracking(QtCore.QThread):

    def __init__(self, queue_capture, queue_tracking, queue_tracking_for_plate, queue_tracking_for_brand,
                 queue_tracking_for_color, queue_tracking_for_speed, queue_tracking_for_count):
        super().__init__()
        self.__thread_active = False

        # queue
        self.queue_capture = queue_capture
        self.queue_tracking = queue_tracking
        self.queue_tracking_for_plate = queue_tracking_for_plate
        self.queue_tracking_for_brand = queue_tracking_for_brand
        self.queue_tracking_for_color = queue_tracking_for_color
        self.queue_tracking_for_speed = queue_tracking_for_speed
        self.queue_tracking_for_count = queue_tracking_for_count

        # tracking
        self.tracking = Tracking()
        self.setup_tracking()

    def setup_tracking(self):
        weights = "Weight/yolov5s.pt"
        classes = [2, 3, 7]
        conf = 0.5
        imgsz = 640
        device = config.device
        self.tracking.setup_model(weights, classes, conf, imgsz, device)

    def put_to_queue(self, q, thing_to_put):
        if q.qsize() < 1:
            q.put(thing_to_put)

    def run(self):
        self.__thread_active = True
        print('Starting Tracking Thread...')
        while self.__thread_active:
            if self.queue_capture.qsize() > 0:
                frame = self.queue_capture.get()
                frame_copy = frame.copy()
                id_dict = self.tracking.detect(frame)
                raw_id_dict = id_dict.copy()
                self.put_to_queue(self.queue_tracking_for_count, [frame_copy, raw_id_dict])
                list_id = list(id_dict.keys())
                for k in list_id:
                    category = id_dict[k][-1]
                    if int(category) == 3:
                        del id_dict[k]
                self.put_to_queue(self.queue_tracking, [frame_copy, id_dict])
                self.put_to_queue(self.queue_tracking_for_brand, [frame, id_dict])
                self.put_to_queue(self.queue_tracking_for_color, [frame, id_dict])
                self.put_to_queue(self.queue_tracking_for_plate, [frame_copy, id_dict])
                self.put_to_queue(self.queue_tracking_for_speed, [frame, id_dict])

            QtCore.QThread.msleep(1)

    def stop(self):
        print('Stopping Capture Thread')
        self.__thread_active = False
