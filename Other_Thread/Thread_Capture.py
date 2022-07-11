from PyQt5 import QtCore
import time
import cv2


class ThreadCapture(QtCore.QThread):

    def __init__(self, queue_capture):
        super().__init__()
        self.queue_capture = queue_capture
        self.__thread_active = False

    def setup(self, source):
        self.source = source
        print(self.source)

    def run(self):
        self.__thread_active = True
        print('Starting Capture Thread...')
        self.cap = cv2.VideoCapture(self.source)
        while self.__thread_active:
            ret, frame = self.cap.read()
            if not ret:
                break
            if self.queue_capture.qsize() < 1:
                self.queue_capture.put(frame)
                QtCore.QThread.msleep(100)

    def stop(self):
        print('Stopping Capture Thread')
        self.__thread_active = False
