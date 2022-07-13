from PyQt5 import QtCore
import time
import cv2


class ThreadCapture(QtCore.QThread):

    def __init__(self, queue_capture, source):
        super().__init__()
        self.queue_capture = queue_capture
        self.source = source.replace('\\', '/')
        self.__thread_active = False

    def run(self):
        self.__thread_active = True
        print('Starting Capture Thread...')
        self.cap = cv2.VideoCapture(self.source)
        count = 0
        fps = 0
        t = time.time()
        while self.__thread_active:
            ret, frame = self.cap.read()
            if time.time() - t > 1:
                fps = count
                t = time.time()
                count = 0
            if not ret:
                print('Capture Thread: No frame')
                self.cap = cv2.VideoCapture(self.source)
                time.sleep(3)
                continue
            count += 1
            cv2.putText(frame, str(fps), (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            if self.queue_capture.qsize() < 1 and frame is not None:
                self.queue_capture.put(frame)
            QtCore.QThread.msleep(20)

    def stop(self):
        print('Stopping Capture Thread')
        self.__thread_active = False
