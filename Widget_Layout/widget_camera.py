# -*- coding: utf-8 -*-

# self implementation generated from reading ui file '.\widget_camera.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
from Process.Process_Capture import ThreadCapture
from Process.Process_Tracking import ThreadTracking
from Process.Process_Show import ThreadShow
from Process.Process_Brand import ThreadBrand
from Process.Process_Color import ThreadColor
from Process.Process_Plate import ThreadPlate
from Process.Process_Digit import ThreadDigit
from Process.Process_Speed import ThreadSpeed
from Process.Process_Summary import ThreadSummary
from Process.Process_Plate_Color import ThreadPlateColor
from Process.Process_Counting import ThreadCounting
from Process.Process_Save_Video import ThreadSaveVideo

from Widget_Layout.widget_camera_setup import Widget_Camera_Item
from queue import Queue


class Ui_Camera(Widget_Camera_Item):

    def __init__(self):
        super().__init__()
        # queue
        self.queue_capture = Queue()

        # queue tracking
        self.queue_tracking = Queue()
        self.queue_tracking_for_plate = Queue()
        self.queue_tracking_for_brand = Queue()
        self.queue_tracking_for_color = Queue()
        self.queue_tracking_for_speed = Queue()

        # queue output
        self.queue_plate = Queue()
        self.queue_plate_for_plate_color = Queue()
        self.queue_for_tracking_count = Queue()
        self.queue_plate_color = Queue()
        self.queue_brand = Queue()
        self.queue_color = Queue()
        self.queue_digit = Queue()
        self.queue_speed = Queue()
        self.queue_output = Queue()

    def setup(self, id, source):
        self.id = id
        self.source = source

    def create_thread(self):
        self.thread_capture = ThreadCapture(self.queue_capture, self.source)
        self.thread_tracking = ThreadTracking(self.queue_capture, self.queue_tracking, self.queue_tracking_for_plate,
                                              self.queue_tracking_for_brand, self.queue_tracking_for_color,
                                              self.queue_tracking_for_speed, self.queue_for_tracking_count)
        self.thread_plate = ThreadPlate(self.queue_tracking_for_plate, self.queue_plate,
                                        self.queue_plate_for_plate_color)
        self.thread_brand = ThreadBrand(self.queue_tracking_for_brand, self.queue_brand)
        self.thread_color = ThreadColor(self.queue_tracking_for_color, self.queue_color)
        self.thread_digit = ThreadDigit(self.queue_plate, self.queue_digit)
        # self.thread_plate_color = ThreadPlateColor(self.queue_plate_for_plate_color, self.queue_plate_color)
        self.thread_speed = ThreadSpeed(self.queue_tracking_for_speed, self.queue_speed)
        self.thread_counting = ThreadCounting(self.queue_for_tracking_count)
        self.thread_save_video = ThreadSaveVideo()
        self.thread_summary = ThreadSummary(self.queue_color, self.queue_brand, self.queue_digit, self.queue_speed,
                                            self.queue_plate_color)
        self.thread_show = ThreadShow(self.queue_tracking, self.queue_output)

        self.connect_signal()

    def connect_signal(self):
        self.thread_summary.sig_summary.connect(self.thread_show.slot_summary)
        self.thread_counting.sig_video_car.connect(self.thread_save_video.slot_save_video)

    def start_all_thread(self):
        # show frame
        self.group_settings.hide()
        self.camera_frame.show()

        # start thread
        self.thread_capture.start()
        self.thread_tracking.start()
        self.thread_show.start()
        self.thread_plate.start()
        self.thread_counting.start()
        self.thread_save_video.start()
        self.thread_brand.start()
        self.thread_color.start()
        self.thread_digit.start()
        # self.thread_plate_color.start()
        self.thread_speed.start()
        self.thread_summary.start()

    def stop_all_thread(self):
        # stop thread
        self.thread_capture.stop()
        self.thread_tracking.stop()
        self.thread_show.stop()

        # show setting group
        self.camera_frame.clear()
        self.camera_frame.hide()
        self.group_settings.show()

    def paintEvent(self, event):
        if self.queue_output.qsize() > 0:
            current_frame = self.queue_output.get()
            self.show_frame(self.camera_frame, current_frame)
        self.update()

    def show_frame(self, frame_camera, current_frame):
        if current_frame is not None:
            rgb_img = cv2.cvtColor(current_frame, cv2.COLOR_BGR2RGB)
            qt_img = QtGui.QPixmap.fromImage(
                QtGui.QImage(rgb_img.data, rgb_img.shape[1], rgb_img.shape[0], QtGui.QImage.Format_RGB888)).scaled(
                frame_camera.width(), frame_camera.height())
            frame_camera.setPixmap(qt_img)
            frame_camera.setScaledContents(True)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    source = r"D:\ZHuyQuang\Video\a.mp4"
    ui = Ui_Camera("1", source)
    ui.show()
    sys.exit(app.exec_())
