# Form implementation generated from reading ui file 'lab5.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(904, 481)
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        self.image = QtWidgets.QLabel(Form)
        self.image.setGeometry(QtCore.QRect(20, 40, 400, 421))
        self.image.setStyleSheet("background: gray;")
        self.image.setText("")
        self.image.setObjectName("image")
        self.file_browse = QtWidgets.QPushButton(Form)
        self.file_browse.setGeometry(QtCore.QRect(770, 40, 111, 31))
        self.file_browse.setObjectName("file_browse")
        self.filename_edit = QtWidgets.QLineEdit(Form)
        self.filename_edit.setGeometry(QtCore.QRect(450, 40, 311, 31))
        self.filename_edit.setObjectName("filename_edit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(26, 10, 261, 20))
        self.label.setObjectName("label")
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(450, 80, 431, 191))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Harris = QtWidgets.QPushButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Harris.setFont(font)
        self.Harris.setObjectName("Harris")
        self.verticalLayout.addWidget(self.Harris)
        self.SIFT = QtWidgets.QPushButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SIFT.setFont(font)
        self.SIFT.setObjectName("SIFT")
        self.verticalLayout.addWidget(self.SIFT)
        self.SURF = QtWidgets.QPushButton(self.groupBox_4)
        self.SURF.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SURF.setFont(font)
        self.SURF.setObjectName("SURF")
        self.verticalLayout.addWidget(self.SURF)
        self.FAST = QtWidgets.QPushButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.FAST.setFont(font)
        self.FAST.setObjectName("FAST")
        self.verticalLayout.addWidget(self.FAST)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(450, 280, 431, 181))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.MOG2 = QtWidgets.QPushButton(self.groupBox)
        self.MOG2.setObjectName("MOG2")
        self.horizontalLayout.addWidget(self.MOG2)
        self.KNN = QtWidgets.QPushButton(self.groupBox)
        self.KNN.setObjectName("KNN")
        self.horizontalLayout.addWidget(self.KNN)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.motionBlur = QtWidgets.QPushButton(self.groupBox_2)
        self.motionBlur.setObjectName("motionBlur")
        self.horizontalLayout_2.addWidget(self.motionBlur)
        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Lab5"))
        self.file_browse.setText(_translate("Form", "Загрузить"))
        self.label.setText(_translate("Form", "Оригинальное изображение"))
        self.groupBox_4.setTitle(_translate("Form", "Детекторы"))
        self.Harris.setText(_translate("Form", "Харриса"))
        self.SIFT.setText(_translate("Form", "SIFT"))
        self.SURF.setText(_translate("Form", "SURF"))
        self.FAST.setText(_translate("Form", "FAST"))
        self.groupBox_3.setTitle(_translate("Form", "Видео"))
        self.groupBox.setTitle(_translate("Form", "Вычитание заднего фона"))
        self.MOG2.setText(_translate("Form", "MOG2"))
        self.KNN.setText(_translate("Form", "KNN"))
        self.motionBlur.setText(_translate("Form", "Размытие движущихся объектов"))
