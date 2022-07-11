# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\camera_item.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Widget_Camera_Item(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi()
        self.camera_frame.hide()

    def setupUi(self):
        self.setObjectName("form_camera")
        self.resize(454, 247)
        self.setStyleSheet("background-color: beige;")
        self.layout_main = QtWidgets.QGridLayout(self)
        self.layout_main.setContentsMargins(0, 0, 0, 0)
        self.layout_main.setSpacing(0)
        self.layout_main.setObjectName("layout_main")
        self.group_settings = QtWidgets.QGroupBox(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_settings.sizePolicy().hasHeightForWidth())
        self.group_settings.setSizePolicy(sizePolicy)
        self.group_settings.setMinimumSize(QtCore.QSize(0, 0))
        self.group_settings.setTitle("")
        self.group_settings.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.group_settings.setFlat(False)
        self.group_settings.setObjectName("group_settings")
        self.layout_settings = QtWidgets.QGridLayout(self.group_settings)
        self.layout_settings.setObjectName("layout_settings")
        self.btn_cancel = QtWidgets.QPushButton(self.group_settings)
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_cancel.setStyleSheet("border: 1px solid red;")
        self.layout_settings.addWidget(self.btn_cancel, 2, 3, 1, 2)
        self.btn_apply = QtWidgets.QPushButton(self.group_settings)
        self.btn_apply.setObjectName("btn_apply")
        self.btn_apply.setStyleSheet("border: 1px solid green;")
        self.layout_settings.addWidget(self.btn_apply, 2, 0, 1, 2)
        self.label_show = QtWidgets.QLabel(self.group_settings)
        self.label_show.setObjectName("label_show")
        self.layout_settings.addWidget(self.label_show, 1, 3, 1, 1)
        self.txt_rtsp = QtWidgets.QLineEdit(self.group_settings)
        self.txt_rtsp.setObjectName("txt_rtsp")
        self.layout_settings.addWidget(self.txt_rtsp, 0, 4, 1, 1)
        self.cb_display = QtWidgets.QCheckBox(self.group_settings)
        self.cb_display.setText("")
        self.cb_display.setObjectName("cb_display")
        self.layout_settings.addWidget(self.cb_display, 1, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(12, 12, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.layout_settings.addItem(spacerItem, 0, 2, 1, 1)
        self.label_rtsp = QtWidgets.QLabel(self.group_settings)
        self.label_rtsp.setObjectName("label_rtsp")
        self.layout_settings.addWidget(self.label_rtsp, 0, 3, 1, 1)
        self.txt_camera_id = QtWidgets.QLineEdit(self.group_settings)
        self.txt_camera_id.setObjectName("txt_camera_id")
        self.layout_settings.addWidget(self.txt_camera_id, 0, 1, 1, 1)
        self.label_camera_id = QtWidgets.QLabel(self.group_settings)
        self.label_camera_id.setObjectName("label_camera_id")
        self.layout_settings.addWidget(self.label_camera_id, 0, 0, 1, 1)
        self.combo_features = QtWidgets.QComboBox(self.group_settings)
        self.combo_features.setObjectName("combo_features")
        self.combo_features.addItem("")
        self.combo_features.addItem("")
        self.layout_settings.addWidget(self.combo_features, 1, 0, 1, 2)
        self.layout_main.addWidget(self.group_settings, 0, 0, 1, 2)
        self.camera_frame = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.camera_frame.sizePolicy().hasHeightForWidth())
        self.camera_frame.setSizePolicy(sizePolicy)
        self.camera_frame.setStyleSheet("border : 2px solid red;")

        self.camera_frame.setObjectName("camera_frame")
        self.layout_main.addWidget(self.camera_frame, 1, 0, 1, 2)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("form_camera", "Form"))
        self.label_show.setText(_translate("form_camera", "Hiển thị:"))
        self.label_rtsp.setText(_translate("form_camera", "RTPS: "))
        self.label_camera_id.setText(_translate("form_camera", "CamID"))
        self.combo_features.setItemText(0, _translate("form_camera", "Phát hiện biển số xe"))
        self.btn_apply.setText(_translate("form_camera", "Áp dụng"))
        self.btn_cancel.setText(_translate("form_camera", "Hủy"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Widget_Camera_Item()
    ui.show()
    sys.exit(app.exec_())
