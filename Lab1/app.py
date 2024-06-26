from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QWidget


class Ui_Form(QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(899, 800)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(440, 80, 401, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.deviceSize = QtWidgets.QLabel(self.layoutWidget)
        self.deviceSize.setObjectName("deviceSize")
        self.verticalLayout.addWidget(self.deviceSize)
        self.imageSize = QtWidgets.QLabel(self.layoutWidget)
        self.imageSize.setObjectName("imageSize")
        self.verticalLayout.addWidget(self.imageSize)
        self.format = QtWidgets.QLabel(self.layoutWidget)
        self.format.setObjectName("format")
        self.verticalLayout.addWidget(self.format)
        self.colorDepth = QtWidgets.QLabel(self.layoutWidget)
        self.colorDepth.setObjectName("colorDepth")
        self.verticalLayout.addWidget(self.colorDepth)
        self.colorModel = QtWidgets.QLabel(self.layoutWidget)
        self.colorModel.setObjectName("colorModel")
        self.verticalLayout.addWidget(self.colorModel)
        self.creationDate = QtWidgets.QLabel(self.layoutWidget)
        self.creationDate.setObjectName("creationDate")
        self.verticalLayout.addWidget(self.creationDate)
        self.image = QtWidgets.QLabel(Form)
        self.image.setGeometry(QtCore.QRect(20, 20, 400, 400))
        self.image.setStyleSheet("background: gray;")
        self.image.setText("")
        self.image.setObjectName("image")
        self.file_browse = QtWidgets.QPushButton(Form)
        self.file_browse.setGeometry(QtCore.QRect(750, 40, 121, 23))
        self.file_browse.setObjectName("file_browse")
        self.filename_edit = QtWidgets.QLineEdit(Form)
        self.filename_edit.setGeometry(QtCore.QRect(440, 40, 301, 20))
        self.filename_edit.setObjectName("filename_edit")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 450, 311, 291))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_8 = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.groupBox_8.setObjectName("groupBox_8")
        self.h_hsl = QtWidgets.QLineEdit(self.groupBox_8)
        self.h_hsl.setGeometry(QtCore.QRect(30, 20, 41, 20))
        self.h_hsl.setObjectName("h_hsl")
        self.label_23 = QtWidgets.QLabel(self.groupBox_8)
        self.label_23.setGeometry(QtCore.QRect(10, 20, 21, 21))
        self.label_23.setObjectName("label_23")
        self.s_hsl = QtWidgets.QLineEdit(self.groupBox_8)
        self.s_hsl.setGeometry(QtCore.QRect(30, 50, 41, 20))
        self.s_hsl.setObjectName("s_hsl")
        self.l_hsl = QtWidgets.QLineEdit(self.groupBox_8)
        self.l_hsl.setGeometry(QtCore.QRect(30, 80, 41, 20))
        self.l_hsl.setObjectName("l_hsl")
        self.label_24 = QtWidgets.QLabel(self.groupBox_8)
        self.label_24.setGeometry(QtCore.QRect(10, 50, 21, 21))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.groupBox_8)
        self.label_25.setGeometry(QtCore.QRect(10, 80, 21, 21))
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.groupBox_8, 1, 2, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.c_cmyk = QtWidgets.QLineEdit(self.groupBox_2)
        self.c_cmyk.setGeometry(QtCore.QRect(30, 20, 41, 20))
        self.c_cmyk.setObjectName("c_cmyk")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(10, 20, 21, 21))
        self.label_9.setObjectName("label_9")
        self.m_cmyk = QtWidgets.QLineEdit(self.groupBox_2)
        self.m_cmyk.setGeometry(QtCore.QRect(30, 50, 41, 20))
        self.m_cmyk.setObjectName("m_cmyk")
        self.y_cmyk = QtWidgets.QLineEdit(self.groupBox_2)
        self.y_cmyk.setGeometry(QtCore.QRect(30, 80, 41, 20))
        self.y_cmyk.setObjectName("y_cmyk")
        self.k_cmyk = QtWidgets.QLineEdit(self.groupBox_2)
        self.k_cmyk.setGeometry(QtCore.QRect(30, 110, 41, 20))
        self.k_cmyk.setObjectName("k_cmyk")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(10, 50, 21, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(10, 80, 21, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(10, 110, 21, 21))
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.groupBox_2, 1, 1, 1, 1)
        self.groupBox_12 = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.groupBox_12.setObjectName("groupBox_12")
        self.r_rgb = QtWidgets.QLineEdit(self.groupBox_12)
        self.r_rgb.setGeometry(QtCore.QRect(30, 20, 41, 20))
        self.r_rgb.setObjectName("r_rgb")
        self.label_44 = QtWidgets.QLabel(self.groupBox_12)
        self.label_44.setGeometry(QtCore.QRect(10, 20, 21, 21))
        self.label_44.setObjectName("label_44")
        self.g_rgb = QtWidgets.QLineEdit(self.groupBox_12)
        self.g_rgb.setGeometry(QtCore.QRect(30, 50, 41, 20))
        self.g_rgb.setObjectName("g_rgb")
        self.b_rgb = QtWidgets.QLineEdit(self.groupBox_12)
        self.b_rgb.setGeometry(QtCore.QRect(30, 80, 41, 20))
        self.b_rgb.setObjectName("b_rgb")
        self.label_45 = QtWidgets.QLabel(self.groupBox_12)
        self.label_45.setGeometry(QtCore.QRect(10, 50, 21, 21))
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.groupBox_12)
        self.label_46.setGeometry(QtCore.QRect(10, 80, 21, 21))
        self.label_46.setObjectName("label_46")
        self.gridLayout.addWidget(self.groupBox_12, 1, 0, 1, 1)
        self.groupBox_9 = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.groupBox_9.setObjectName("groupBox_9")
        self.l_lab = QtWidgets.QLineEdit(self.groupBox_9)
        self.l_lab.setGeometry(QtCore.QRect(30, 20, 41, 20))
        self.l_lab.setObjectName("l_lab")
        self.label_32 = QtWidgets.QLabel(self.groupBox_9)
        self.label_32.setGeometry(QtCore.QRect(10, 20, 21, 21))
        self.label_32.setObjectName("label_32")
        self.a_lab = QtWidgets.QLineEdit(self.groupBox_9)
        self.a_lab.setGeometry(QtCore.QRect(30, 50, 41, 20))
        self.a_lab.setObjectName("a_lab")
        self.b_lab = QtWidgets.QLineEdit(self.groupBox_9)
        self.b_lab.setGeometry(QtCore.QRect(30, 80, 41, 20))
        self.b_lab.setObjectName("b_lab")
        self.label_33 = QtWidgets.QLabel(self.groupBox_9)
        self.label_33.setGeometry(QtCore.QRect(10, 50, 21, 21))
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.groupBox_9)
        self.label_34.setGeometry(QtCore.QRect(10, 80, 21, 21))
        self.label_34.setObjectName("label_34")
        self.gridLayout.addWidget(self.groupBox_9, 2, 0, 1, 1)
        self.groupBox_10 = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.groupBox_10.setObjectName("groupBox_10")
        self.h_hsv = QtWidgets.QLineEdit(self.groupBox_10)
        self.h_hsv.setGeometry(QtCore.QRect(30, 20, 41, 20))
        self.h_hsv.setObjectName("h_hsv")
        self.label_35 = QtWidgets.QLabel(self.groupBox_10)
        self.label_35.setGeometry(QtCore.QRect(10, 20, 21, 21))
        self.label_35.setObjectName("label_35")
        self.s_hsv = QtWidgets.QLineEdit(self.groupBox_10)
        self.s_hsv.setGeometry(QtCore.QRect(30, 50, 41, 20))
        self.s_hsv.setObjectName("s_hsv")
        self.v_hsv = QtWidgets.QLineEdit(self.groupBox_10)
        self.v_hsv.setGeometry(QtCore.QRect(30, 80, 41, 20))
        self.v_hsv.setObjectName("v_hsv")
        self.label_36 = QtWidgets.QLabel(self.groupBox_10)
        self.label_36.setGeometry(QtCore.QRect(10, 50, 21, 21))
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.groupBox_10)
        self.label_37.setGeometry(QtCore.QRect(10, 80, 21, 21))
        self.label_37.setObjectName("label_37")
        self.gridLayout.addWidget(self.groupBox_10, 2, 1, 1, 1)
        self.groupBox_11 = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.groupBox_11.setObjectName("groupBox_11")
        self.y_ycbcr = QtWidgets.QLineEdit(self.groupBox_11)
        self.y_ycbcr.setGeometry(QtCore.QRect(30, 20, 41, 20))
        self.y_ycbcr.setObjectName("y_ycbcr")
        self.label_38 = QtWidgets.QLabel(self.groupBox_11)
        self.label_38.setGeometry(QtCore.QRect(10, 20, 21, 21))
        self.label_38.setObjectName("label_38")
        self.cb_ycbcr = QtWidgets.QLineEdit(self.groupBox_11)
        self.cb_ycbcr.setGeometry(QtCore.QRect(30, 50, 41, 20))
        self.cb_ycbcr.setObjectName("cb_ycbcr")
        self.cr_ycbcr = QtWidgets.QLineEdit(self.groupBox_11)
        self.cr_ycbcr.setGeometry(QtCore.QRect(30, 80, 41, 20))
        self.cr_ycbcr.setObjectName("cr_ycbcr")
        self.label_39 = QtWidgets.QLabel(self.groupBox_11)
        self.label_39.setGeometry(QtCore.QRect(10, 50, 21, 21))
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.groupBox_11)
        self.label_40.setGeometry(QtCore.QRect(10, 80, 21, 21))
        self.label_40.setObjectName("label_40")
        self.gridLayout.addWidget(self.groupBox_11, 2, 2, 1, 1)
        self.color = QtWidgets.QLabel(Form)
        self.color.setGeometry(QtCore.QRect(360, 460, 60, 60))
        self.color.setStyleSheet("background: rgb(255, 255, 255);")
        self.color.setText("")
        self.color.setObjectName("color")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Lab1"))
        self.deviceSize.setText(_translate("Form", "Размер на диске:"))
        self.imageSize.setText(_translate("Form", "Разрешение:"))
        self.format.setText(_translate("Form", "Формат файла:"))
        self.colorDepth.setText(_translate("Form", "Глубина цвета:"))
        self.colorModel.setText(_translate("Form", "Цветовая модель:"))
        self.creationDate.setText(_translate("Form", "Дата создания:"))
        self.file_browse.setText(_translate("Form", "Загрузить"))
        self.groupBox_8.setTitle(_translate("Form", "HSL"))
        self.label_23.setText(_translate("Form", "H"))
        self.label_24.setText(_translate("Form", "S"))
        self.label_25.setText(_translate("Form", "L"))
        self.groupBox_2.setTitle(_translate("Form", "CMYK"))
        self.label_9.setText(_translate("Form", "C"))
        self.label_10.setText(_translate("Form", "M"))
        self.label_11.setText(_translate("Form", "Y"))
        self.label_12.setText(_translate("Form", "K"))
        self.groupBox_12.setTitle(_translate("Form", "RGB"))
        self.r_rgb.setText(_translate("Form", "255"))
        self.label_44.setText(_translate("Form", "R"))
        self.g_rgb.setText(_translate("Form", "255"))
        self.b_rgb.setText(_translate("Form", "255"))
        self.label_45.setText(_translate("Form", "G"))
        self.label_46.setText(_translate("Form", "B"))
        self.groupBox_9.setTitle(_translate("Form", "LAB"))
        self.label_32.setText(_translate("Form", "L"))
        self.label_33.setText(_translate("Form", "A"))
        self.label_34.setText(_translate("Form", "B"))
        self.groupBox_10.setTitle(_translate("Form", "HSV"))
        self.label_35.setText(_translate("Form", "H"))
        self.label_36.setText(_translate("Form", "S"))
        self.label_37.setText(_translate("Form", "V"))
        self.groupBox_11.setTitle(_translate("Form", "YCbCr"))
        self.label_38.setText(_translate("Form", "Y"))
        self.label_39.setText(_translate("Form", "Cb"))
        self.label_40.setText(_translate("Form", "Cr"))

