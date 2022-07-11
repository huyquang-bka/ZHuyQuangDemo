# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1382, 904)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(0, 85, 127);")
        self.centralwidget.setObjectName("centralwidget")
        self.layout_main = QtWidgets.QGridLayout(self.centralwidget)
        self.layout_main.setObjectName("layout_main")
        self.menu = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu.sizePolicy().hasHeightForWidth())
        self.menu.setSizePolicy(sizePolicy)
        self.menu.setMinimumSize(QtCore.QSize(300, 0))
        self.menu.setStyleSheet("")
        self.menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu.setObjectName("menu")
        self.gridLayout = QtWidgets.QGridLayout(self.menu)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setStyleSheet("QGroupBox{\n"
                                    "    background-color: rgb(170, 170, 0);\n"
                                    "    border: none;\n"
                                    "    border-radius: 10px\n"
                                    "}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.qlabel_vehicle_count_bike = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qlabel_vehicle_count_bike.sizePolicy().hasHeightForWidth())
        self.qlabel_vehicle_count_bike.setSizePolicy(sizePolicy)
        self.qlabel_vehicle_count_bike.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.qlabel_vehicle_count_bike.setFont(font)
        self.qlabel_vehicle_count_bike.setStyleSheet("background-color: rgb(0, 0, 45);\n"
                                                     "color: white;")
        self.qlabel_vehicle_count_bike.setAlignment(QtCore.Qt.AlignCenter)
        self.qlabel_vehicle_count_bike.setObjectName("qlabel_vehicle_count_bike")
        self.gridLayout_2.addWidget(self.qlabel_vehicle_count_bike, 1, 1, 1, 1)
        self.qlabel_count_bike = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qlabel_count_bike.sizePolicy().hasHeightForWidth())
        self.qlabel_count_bike.setSizePolicy(sizePolicy)
        self.qlabel_count_bike.setMinimumSize(QtCore.QSize(100, 100))
        self.qlabel_count_bike.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.qlabel_count_bike.setFont(font)
        self.qlabel_count_bike.setStyleSheet("background-color: rgb(170, 170, 170)")
        self.qlabel_count_bike.setLineWidth(0)
        self.qlabel_count_bike.setText("")
        self.qlabel_count_bike.setAlignment(QtCore.Qt.AlignCenter)
        self.qlabel_count_bike.setObjectName("qlabel_count_bike")
        self.gridLayout_2.addWidget(self.qlabel_count_bike, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.qlabel_vehicle_count_car = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qlabel_vehicle_count_car.sizePolicy().hasHeightForWidth())
        self.qlabel_vehicle_count_car.setSizePolicy(sizePolicy)
        self.qlabel_vehicle_count_car.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.qlabel_vehicle_count_car.setFont(font)
        self.qlabel_vehicle_count_car.setStyleSheet("background-color: rgb(0, 0, 45);\n"
                                                    "color: white;")
        self.qlabel_vehicle_count_car.setAlignment(QtCore.Qt.AlignCenter)
        self.qlabel_vehicle_count_car.setObjectName("qlabel_vehicle_count_car")
        self.gridLayout_2.addWidget(self.qlabel_vehicle_count_car, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        self.qlabel_count_car = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qlabel_count_car.sizePolicy().hasHeightForWidth())
        self.qlabel_count_car.setSizePolicy(sizePolicy)
        self.qlabel_count_car.setMinimumSize(QtCore.QSize(100, 100))
        self.qlabel_count_car.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.qlabel_count_car.setFont(font)
        self.qlabel_count_car.setStyleSheet("background-color: rgb(170, 170, 170)")
        self.qlabel_count_car.setText("")
        self.qlabel_count_car.setAlignment(QtCore.Qt.AlignCenter)
        self.qlabel_count_car.setObjectName("qlabel_count_car")
        self.gridLayout_2.addWidget(self.qlabel_count_car, 3, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_2.addItem(spacerItem2, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 8, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)
        self.btn_search = QtWidgets.QPushButton(self.menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_search.sizePolicy().hasHeightForWidth())
        self.btn_search.setSizePolicy(sizePolicy)
        self.btn_search.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_search.setStyleSheet("QPushButton{\n"
                                      "    background-color: rgb(170, 170, 0);\n"
                                      "    border: none;\n"
                                      "    border-radius: 10px\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "    background-color: rgb(109, 109, 0);\n"
                                      "    border: none;\n"
                                      "    border-radius: 10px\n"
                                      "}")
        self.btn_search.setObjectName("btn_search")
        self.gridLayout.addWidget(self.btn_search, 5, 0, 1, 1)
        self.btn_start_app = QtWidgets.QPushButton(self.menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_start_app.sizePolicy().hasHeightForWidth())
        self.btn_start_app.setSizePolicy(sizePolicy)
        self.btn_start_app.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_start_app.setStyleSheet("QPushButton{\n"
                                         "    background-color: rgb(170, 170, 0);\n"
                                         "    border: none;\n"
                                         "    border-radius: 10px\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "    background-color: rgb(109, 109, 0);\n"
                                         "    border: none;\n"
                                         "    border-radius: 10px\n"
                                         "}")
        self.btn_start_app.setObjectName("btn_start_app")
        self.gridLayout.addWidget(self.btn_start_app, 3, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem4, 6, 0, 1, 1)
        self.qlabel_logo_atin = QtWidgets.QLabel(self.menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qlabel_logo_atin.sizePolicy().hasHeightForWidth())
        self.qlabel_logo_atin.setSizePolicy(sizePolicy)
        self.qlabel_logo_atin.setMinimumSize(QtCore.QSize(0, 120))
        self.qlabel_logo_atin.setMaximumSize(QtCore.QSize(16777215, 120))
        self.qlabel_logo_atin.setStyleSheet("background: gray\n"
                                            "")
        self.qlabel_logo_atin.setText("")
        self.qlabel_logo_atin.setObjectName("qlabel_logo_atin")
        self.gridLayout.addWidget(self.qlabel_logo_atin, 0, 0, 1, 1)
        self.btn_setup_layout = QtWidgets.QPushButton(self.menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_setup_layout.sizePolicy().hasHeightForWidth())
        self.btn_setup_layout.setSizePolicy(sizePolicy)
        self.btn_setup_layout.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_setup_layout.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.btn_setup_layout.setFont(font)
        self.btn_setup_layout.setMouseTracking(False)
        self.btn_setup_layout.setStyleSheet("QPushButton{\n"
                                            "    background-color: rgb(170, 170, 0);\n"
                                            "    border: none;\n"
                                            "    border-radius: 10px\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "    background-color: rgb(109, 109, 0);\n"
                                            "    border: none;\n"
                                            "    border-radius: 10px\n"
                                            "}")
        self.btn_setup_layout.setInputMethodHints(QtCore.Qt.ImhNone)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Project-1/icon/setup_layout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_setup_layout.setIcon(icon)
        self.btn_setup_layout.setIconSize(QtCore.QSize(25, 25))
        self.btn_setup_layout.setDefault(False)
        self.btn_setup_layout.setFlat(False)
        self.btn_setup_layout.setObjectName("btn_setup_layout")
        self.gridLayout.addWidget(self.btn_setup_layout, 2, 0, 1, 1)
        self.btn_stop_app = QtWidgets.QPushButton(self.menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_stop_app.sizePolicy().hasHeightForWidth())
        self.btn_stop_app.setSizePolicy(sizePolicy)
        self.btn_stop_app.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_stop_app.setStyleSheet("QPushButton{\n"
                                        "    background-color: rgb(170, 170, 0);\n"
                                        "    border: none;\n"
                                        "    border-radius: 10px\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(109, 109, 0);\n"
                                        "    border: none;\n"
                                        "    border-radius: 10px\n"
                                        "}")
        self.btn_stop_app.setObjectName("btn_stop_app")
        self.gridLayout.addWidget(self.btn_stop_app, 4, 0, 1, 1)
        self.layout_main.addWidget(self.menu, 0, 0, 1, 1)
        self.scrollArea_info = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_info.sizePolicy().hasHeightForWidth())
        self.scrollArea_info.setSizePolicy(sizePolicy)
        self.scrollArea_info.setMinimumSize(QtCore.QSize(0, 250))
        self.scrollArea_info.setStyleSheet("background-color: rgb(0, 63, 93);")
        self.scrollArea_info.setWidgetResizable(True)
        self.scrollArea_info.setObjectName("scrollArea_info")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1362, 248))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea_info.setWidget(self.scrollAreaWidgetContents)
        self.layout_main.addWidget(self.scrollArea_info, 1, 0, 1, 3)
        self.frame_cameras = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_cameras.sizePolicy().hasHeightForWidth())
        self.frame_cameras.setSizePolicy(sizePolicy)
        self.frame_cameras.setStyleSheet("background-color: rgb(0, 71, 104);")
        self.frame_cameras.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cameras.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cameras.setObjectName("frame_cameras")
        self.layout_main.addWidget(self.frame_cameras, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.qlabel_vehicle_count_bike.setText(_translate("MainWindow", "0"))
        self.qlabel_vehicle_count_car.setText(_translate("MainWindow", "0"))
        self.btn_search.setText(_translate("MainWindow", "Search"))
        self.btn_start_app.setText(_translate("MainWindow", "Start App"))
        self.btn_setup_layout.setText(_translate("MainWindow", "Setup Layout"))
        self.btn_stop_app.setText(_translate("MainWindow", "Stop App"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
