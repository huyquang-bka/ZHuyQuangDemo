from PyQt5 import QtCore
import time
import cv2
from Yolov5.detect_yolov5 import Tracking


class ThreadSaveVideo(QtCore.QThread):

    def __init__(self):
        super().__init__()
        self.__thread_active = False

        self.id_dict = {}

        self.time_video = 3  # seconds
        self.w = 640
        self.h = 480
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')

    def slot_save_video(self, ls):
        k, v = ls
        list_key = list(self.id_dict.keys())
        if k not in list_key:
            self.id_dict[k] = v

    def run(self):
        self.__thread_active = True
        print('Starting Save Video Thread...')
        old_id_list = []
        while self.__thread_active:
            list_key = list(self.id_dict.keys())
            for k in list_key:
                if k in old_id_list:
                    continue
                v = self.id_dict[k]
                if len(v) > 0:
                    fps = len(v) // self.time_video
                    writer = cv2.VideoWriter(f'Video_Storage/{k}.avi', self.fourcc, fps, (self.w, self.h))
                    for frame in v:
                        writer.write(frame)
                    del self.id_dict[k]
                    old_id_list.append(k)
                    writer.release()
            QtCore.QThread.msleep(1)

    def stop(self):
        print('Stopping Save Video Thread')
        self.__thread_active = False
