from PyQt5 import QtCore
import time
import cv2
from Yolov5.detect_yolov5 import Detection
from Polygon.Polygon import plate_polygon, detect_polygon
import config


class ThreadPlate(QtCore.QThread):

    def __init__(self, queue_tracking_for_plate, queue_plate, queue_plate_for_plate_color):
        super().__init__()
        self.__thread_active = False

        # queue
        self.queue_tracking_for_plate = queue_tracking_for_plate
        self.queue_plate = queue_plate
        self.queue_plate_for_plate_color = queue_plate_for_plate_color

        # tracking
        self.plate_detection = Detection()
        self.setup_plate_detection()

    def setup_plate_detection(self):
        weights = "Weight/lp.pt"
        classes = [0]
        conf = 0.5
        imgsz = 256
        device = config.device
        self.plate_detection.setup_model(weights, classes, conf, imgsz, device)

    def is_in_plate_zone(self, box):
        x1, y1, x2, y2 = box
        return cv2.pointPolygonTest(plate_polygon, ((x1 + x2) // 2, y2), False) > 0

    def is_in_detect_zone(self, box):
        x1, y1, x2, y2 = box
        return cv2.pointPolygonTest(detect_polygon, ((x1 + x2) // 2, y2), False) > 0

    def run(self):
        self.__thread_active = True
        print('Starting Plate Thread...')
        while self.__thread_active:
            if self.queue_tracking_for_plate.qsize() > 0:
                frame, id_dict = self.queue_tracking_for_plate.get()
                plate_dict = {}
                for id, bbox in id_dict.items():
                    box = bbox[:4]
                    x1, y1, x2, y2, cls = bbox
                    if int(cls) not in [2, 7] or not self.is_in_detect_zone(box):
                        continue
                    plate_box = []
                    crop = frame[y1:y2, x1:x2]
                    if self.is_in_plate_zone(box):
                        plate_list = self.plate_detection.detect(crop)
                        if plate_list:
                            plate_box = plate_list[0]
                    plate_dict[id] = [box, plate_box]
                if self.queue_plate.qsize() < 1:
                    self.queue_plate.put([frame, plate_dict])
                if self.queue_plate_for_plate_color.qsize() < 1:
                    self.queue_plate_for_plate_color.put([frame, plate_dict])
            QtCore.QThread.msleep(1)

    def stop(self):
        print('Stopping Plate Thread')
        self.__thread_active = False
