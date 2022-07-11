# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'UI\widget_search.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from Other_Thread.Thread_Capture import ThreadCapture
from queue import Queue
import pandas as pd
import sqlite3
import cv2


class Ui_Search(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

        # connect
        self.txt_search_plate.textChanged.connect(self.slot_query)
        self.table.doubleClicked.connect(self.open_image)
        self.btn_start_video.clicked.connect(self.start_video)

        self.db = 'Database/atin.db'

        # queue
        self.queue_capture = Queue()

        # thread
        self.thread_capture = ThreadCapture(self.queue_capture)

    def db_to_df(self):
        self.conn = sqlite3.connect(self.db)
        self.df = pd.read_sql_query("SELECT * FROM information", self.conn)
        self.df = self.df.sort_values(by=['id_car'])

    def show_table(self):
        df = self.df
        self.table.setRowCount(len(df))
        self.table.setColumnCount(len(df.columns))
        self.table.setHorizontalHeaderLabels(df.columns)
        header = self.table.horizontalHeader()
        self.table.verticalHeader().setVisible(False)
        for i in range(df.columns.size):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
            # header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        for i in range(len(df)):
            for j in range(len(df.columns)):
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(str(df.iloc[i, j])))

    def open_image(self, item):
        self.btn_start_video.setEnabled(True)
        row = item.row()
        data = self.df.iloc[row]
        id = data[0]
        plate = data[1]
        img_path = r"Crop/{}.jpg".format(id)
        self.video_path = r"Video_Storage/{}.avi".format(id)
        self.qlabel_img_plate.setText(plate)
        self.show_image(img_path)

    def show_image(self, img_path):
        try:
            self.thread_capture.stop()
        except:
            pass
        img = QtGui.QImage(img_path)
        pixmap = QtGui.QPixmap.fromImage(img)
        self.qlabel_image.setPixmap(pixmap)
        self.qlabel_image.setScaledContents(True)
        self.qlabel_video.setPixmap(pixmap)
        self.qlabel_video.setScaledContents(True)

    def show_video(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        qimg = QtGui.QImage(rgb.data, rgb.shape[1], rgb.shape[0], QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(qimg)
        self.qlabel_video.setPixmap(pixmap)
        self.qlabel_video.setScaledContents(True)

    def slot_query(self, s):
        if not s:
            print("No query")
            return
        items = self.table.findItems(
            s, QtCore.Qt.MatchContains | QtCore.Qt.MatchRecursive)
        rows = [item.row() for item in items]
        for i in range(self.table.rowCount()):
            self.table.setRowHidden(i, not (i in rows))

    def start_video(self):
        try:
            self.thread_capture.stop()
        except:
            pass
        self.thread_capture.setup(self.video_path)
        self.thread_capture.start()

    def paintEvent(self, event):
        if self.queue_capture.qsize() > 0:
            frame = self.queue_capture.get()
        else:
            frame = None
        if frame is not None:
            self.show_video(frame)
        self.update()

    def setupUi(self):
        self.setObjectName("self")
        self.resize(1017, 751)
        self.setStyleSheet("background-color: rgb(0, 63, 93);")
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.image = QtWidgets.QGroupBox(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.image.setFont(font)
        self.image.setStyleSheet("color: rgb(190,190,0)")
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setFlat(False)
        self.image.setCheckable(False)
        self.image.setObjectName("image")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.image)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.qlabel_img_plate = QtWidgets.QLabel(self.image)
        self.qlabel_img_plate.setMinimumSize(QtCore.QSize(0, 50))
        self.qlabel_img_plate.setStyleSheet(
            "background: silver; padding: 10px; border-radius: 10px; color: black; font: bold; font-family: Roboto; text-align: center;")
        self.qlabel_img_plate.setText("")
        self.qlabel_img_plate.setObjectName("qlabel_img_plate")
        self.qlabel_img_plate.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout_3.addWidget(self.qlabel_img_plate, 0, 0, 1, 1)
        self.qlabel_image = QtWidgets.QLabel(self.image)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qlabel_image.sizePolicy().hasHeightForWidth())
        self.qlabel_image.setSizePolicy(sizePolicy)
        self.qlabel_image.setStyleSheet("background: black")
        self.qlabel_image.setText("")
        self.qlabel_image.setObjectName("qlabel_image")
        self.gridLayout_3.addWidget(self.qlabel_image, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.image, 0, 1, 1, 1)
        self.video = QtWidgets.QGroupBox(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.video.sizePolicy().hasHeightForWidth())
        self.video.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.video.setFont(font)
        self.video.setStyleSheet("color: rgb(190,190,0)")
        self.video.setAlignment(QtCore.Qt.AlignCenter)
        self.video.setObjectName("video")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.video)
        self.gridLayout_4.setObjectName("gridLayout_4")
        # self.qlabel_video_plate = QtWidgets.QLabel(self.video)
        # self.qlabel_video_plate.setMinimumSize(QtCore.QSize(0, 50))
        # self.qlabel_video_plate.setStyleSheet(
        #     "background: silver; padding: 10px; border-radius: 10px; color: black; font: bold; font-family: Roboto; text-align: center;")
        # self.qlabel_video_plate.setText("")
        # self.qlabel_video_plate.setAlignment(QtCore.Qt.AlignCenter)
        # self.qlabel_video_plate.setObjectName("qlabel_video_plate")
        # self.gridLayout_4.addWidget(self.qlabel_video_plate, 0, 0, 1, 1)
        self.btn_start_video = QtWidgets.QPushButton(self.video)
        self.btn_start_video.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_start_video.setStyleSheet(
            "background: silver; padding: 10px; border-radius: 10px; color: black; font: bold; font-family: Roboto; text-align: center;")
        self.btn_start_video.setText("Start Video")
        self.btn_start_video.setObjectName("btn_start_video")
        self.btn_start_video.setDisabled(True)
        self.gridLayout_4.addWidget(self.btn_start_video, 0, 0, 1, 1)
        self.qlabel_video = QtWidgets.QLabel(self.video)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qlabel_video.sizePolicy().hasHeightForWidth())
        self.qlabel_video.setSizePolicy(sizePolicy)
        self.qlabel_video.setStyleSheet("background: black")
        self.qlabel_video.setText("")
        self.qlabel_video.setObjectName("qlabel_video")
        self.gridLayout_4.addWidget(self.qlabel_video, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.video, 1, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setStyleSheet("background-color: rgb(0, 71, 104);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_search = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_search.sizePolicy().hasHeightForWidth())
        self.btn_search.setSizePolicy(sizePolicy)
        self.btn_search.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_search.setStyleSheet("QPushButton{\n"
                                      "    background-color: rgb(250, 250, 0);\n"
                                      "    border: none;\n"
                                      "    border-radius: 10px\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "    background-color: rgb(109, 109, 0);\n"
                                      "    border: none;\n"
                                      "    border-radius: 10px\n"
                                      "}")
        self.btn_search.setObjectName("btn_search")
        self.gridLayout_2.addWidget(self.btn_search, 0, 2, 1, 1)
        self.qlabel_text_plate = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.qlabel_text_plate.setFont(font)
        self.qlabel_text_plate.setStyleSheet("color: rgb(170, 170, 0);")
        self.qlabel_text_plate.setObjectName("qlabel_text_plate")
        self.gridLayout_2.addWidget(self.qlabel_text_plate, 0, 0, 1, 1)
        self.txt_search_plate = QtWidgets.QLineEdit(self.frame)
        self.txt_search_plate.setPlaceholderText("Search...")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_search_plate.sizePolicy().hasHeightForWidth())
        self.txt_search_plate.setSizePolicy(sizePolicy)
        self.txt_search_plate.setMinimumSize(QtCore.QSize(0, 30))
        self.txt_search_plate.setMaximumSize(QtCore.QSize(16777215, 30))
        self.txt_search_plate.setStyleSheet(
            "background-color:rgb(250, 250, 0); padding: 4px 6px 2px 6px; border-radius: 6px;")
        self.txt_search_plate.setObjectName("txt_search_plate")
        self.gridLayout_2.addWidget(self.txt_search_plate, 0, 1, 1, 1)
        self.table = QtWidgets.QTableWidget(self.frame)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setObjectName("qtable_list_vehicle")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.gridLayout_2.addWidget(self.table, 1, 0, 1, 3)
        self.gridLayout.addWidget(self.frame, 0, 0, 2, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Search", "self"))
        self.image.setTitle(_translate("Search", "Hình ảnh"))
        self.video.setTitle(_translate("Search", "Video"))
        self.btn_search.setText(_translate("Search", "Tìm kiếm"))
        self.qlabel_text_plate.setText(_translate("Search", "Biển số"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    self = QtWidgets.QWidget()
    ui = Ui_Search()
    ui.db = r"D:\Company\ZHuyQuang\Database\atin.db"
    ui.db_to_df()
    ui.show_table()
    ui.show()
    sys.exit(app.exec_())