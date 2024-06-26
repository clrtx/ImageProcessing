# Form implementation generated from reading ui file 'lab4.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(896, 523)
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        self.image = QtWidgets.QLabel(Form)
        self.image.setGeometry(QtCore.QRect(20, 40, 400, 400))
        self.image.setStyleSheet("background: gray;")
        self.image.setText("")
        self.image.setObjectName("image")
        self.file_browse = QtWidgets.QPushButton(Form)
        self.file_browse.setGeometry(QtCore.QRect(330, 470, 91, 31))
        self.file_browse.setObjectName("file_browse")
        self.filename_edit = QtWidgets.QLineEdit(Form)
        self.filename_edit.setGeometry(QtCore.QRect(20, 470, 301, 31))
        self.filename_edit.setObjectName("filename_edit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(26, 10, 261, 20))
        self.label.setObjectName("label")
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(450, 40, 421, 461))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_8.setStyleSheet("")
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.sharpness = QtWidgets.QPushButton(self.groupBox_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sharpness.setFont(font)
        self.sharpness.setObjectName("sharpness")
        self.verticalLayout_5.addWidget(self.sharpness)
        self.verticalLayout.addWidget(self.groupBox_8)
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_7)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 50))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.motionBlurValue = QtWidgets.QSpinBox(self.groupBox)
        self.motionBlurValue.setMaximumSize(QtCore.QSize(70, 16777215))
        self.motionBlurValue.setMinimum(1)
        self.motionBlurValue.setProperty("value", 3)
        self.motionBlurValue.setObjectName("motionBlurValue")
        self.horizontalLayout.addWidget(self.motionBlurValue)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.motionBlur = QtWidgets.QPushButton(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.motionBlur.setFont(font)
        self.motionBlur.setObjectName("motionBlur")
        self.verticalLayout_4.addWidget(self.motionBlur)
        self.verticalLayout.addWidget(self.groupBox_7)
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_9)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.emboss = QtWidgets.QPushButton(self.groupBox_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.emboss.setFont(font)
        self.emboss.setObjectName("emboss")
        self.verticalLayout_6.addWidget(self.emboss)
        self.verticalLayout.addWidget(self.groupBox_9)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.medianFilterValue = QtWidgets.QSpinBox(self.groupBox_2)
        self.medianFilterValue.setMinimumSize(QtCore.QSize(50, 25))
        self.medianFilterValue.setMaximumSize(QtCore.QSize(70, 16777215))
        self.medianFilterValue.setMinimum(1)
        self.medianFilterValue.setSingleStep(2)
        self.medianFilterValue.setProperty("value", 3)
        self.medianFilterValue.setObjectName("medianFilterValue")
        self.horizontalLayout_2.addWidget(self.medianFilterValue)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.medianFilter = QtWidgets.QPushButton(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.medianFilter.setFont(font)
        self.medianFilter.setObjectName("medianFilter")
        self.verticalLayout_2.addWidget(self.medianFilter)
        self.verticalLayout.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_6.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 60))
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cannyFirstTreshold = QtWidgets.QSpinBox(self.groupBox_3)
        self.cannyFirstTreshold.setMinimumSize(QtCore.QSize(0, 24))
        self.cannyFirstTreshold.setMinimum(1)
        self.cannyFirstTreshold.setMaximum(255)
        self.cannyFirstTreshold.setObjectName("cannyFirstTreshold")
        self.horizontalLayout_3.addWidget(self.cannyFirstTreshold)
        self.cannySecondTreshold = QtWidgets.QSpinBox(self.groupBox_3)
        self.cannySecondTreshold.setMinimumSize(QtCore.QSize(0, 24))
        self.cannySecondTreshold.setMinimum(1)
        self.cannySecondTreshold.setMaximum(255)
        self.cannyFirstTreshold.setProperty("value", 50)
        self.cannySecondTreshold.setProperty("value", 150)
        self.cannySecondTreshold.setObjectName("cannySecondTreshold")
        self.horizontalLayout_3.addWidget(self.cannySecondTreshold)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.detectorCanny = QtWidgets.QPushButton(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.detectorCanny.setFont(font)
        self.detectorCanny.setObjectName("detectorCanny")
        self.verticalLayout_3.addWidget(self.detectorCanny)
        self.verticalLayout.addWidget(self.groupBox_6)
        self.groupBox_10 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_10.setTitle("")
        self.groupBox_10.setObjectName("groupBox_10")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.operatorRoberts = QtWidgets.QPushButton(self.groupBox_10)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.operatorRoberts.setFont(font)
        self.operatorRoberts.setObjectName("operatorRoberts")
        self.verticalLayout_7.addWidget(self.operatorRoberts)
        self.verticalLayout.addWidget(self.groupBox_10)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Lab4"))
        self.file_browse.setText(_translate("Form", "Загрузить"))
        self.label.setText(_translate("Form", "Оригинальное изображение"))
        self.sharpness.setText(_translate("Form", "Резкость"))
        self.label_2.setText(_translate("Form", "Размер ядра свертки"))
        self.motionBlur.setText(_translate("Form", "Размытие в движении"))
        self.emboss.setText(_translate("Form", "Тиснение"))
        self.label_3.setText(_translate("Form", "Размер ядра свертки"))
        self.medianFilter.setText(_translate("Form", "Медианная фильтрация"))
        self.groupBox_3.setTitle(_translate("Form", "Границы"))
        self.detectorCanny.setText(_translate("Form", "Детектор Canny"))
        self.operatorRoberts.setText(_translate("Form", "Оператор Робертса"))
