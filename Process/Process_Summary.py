from PyQt5 import QtCore
import time
import cv2


class ThreadSummary(QtCore.QThread):
    sig_summary = QtCore.pyqtSignal(dict)

    def __init__(self, queue_color, queue_brand, queue_digit, queue_speed, queue_plate_color):
        super().__init__()
        self.__thread_active = False

        # queue
        self.queue_color = queue_color
        self.queue_brand = queue_brand
        self.queue_digit = queue_digit
        self.queue_speed = queue_speed
        self.queue_plate_color = queue_plate_color

    def get_info(self, dictionary, summary_dict, index):
        for k, v in dictionary.items():
            if k not in list(summary_dict.keys()):
                summary_dict[k] = ["", "", "", "", ""]
                summary_dict[k][index] = v
            else:
                if v:
                    summary_dict[k][index] = v
        return summary_dict

    def run(self):
        self.__thread_active = True
        print('Starting Summary Thread...')
        summary_dict = {}
        while self.__thread_active:
            if self.queue_color.qsize() > 0:
                color_dict = self.queue_color.get()
                summary_dict = self.get_info(color_dict, summary_dict, 0)
            if self.queue_brand.qsize() > 0:
                brand_dict = self.queue_brand.get()
                summary_dict = self.get_info(brand_dict, summary_dict, 1)
            if self.queue_digit.qsize() > 0:
                digit_dict = self.queue_digit.get()
                summary_dict = self.get_info(digit_dict, summary_dict, 2)
            if self.queue_speed.qsize() > 0:
                speed_dict = self.queue_speed.get()
                summary_dict = self.get_info(speed_dict, summary_dict, 3)
            if self.queue_plate_color.qsize() > 0:
                plate_color_dict = self.queue_plate_color.get()
                summary_dict = self.get_info(plate_color_dict, summary_dict, 4)
            if summary_dict:
                self.sig_summary.emit(summary_dict)
            QtCore.QThread.msleep(1)

    def stop(self):
        print('Stopping Capture Thread')
        self.__thread_active = False
