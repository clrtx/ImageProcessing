import locale
import sys
from io import BytesIO
from pathlib import Path

import PIL
import cv2
import numpy as np
from PIL import Image
from PyQt6.QtCore import QByteArray, QBuffer, QIODevice, QIODeviceBase
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog
from matplotlib import pyplot as plt

from Lab3.app import Ui_Form


class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.file_browse.clicked.connect(self.open_file_dialog)
        self.ui.kernelWidth.setValue(3)
        self.ui.kernelHeight.setValue(3)
        # show the login window
        self.show()

    def open_file_dialog(self):

        filename, ok = QFileDialog.getOpenFileName(
            self,
            "Select a File",
            "D:\\icons\\avatar\\",
            "Images (*.png *.jpg)"
        )
        if filename:
            path = Path(filename)
            self.ui.filename_edit.setText(str(path))
            with PIL.Image.open(filename) as img:
                self.img = img
                self.modImg = img

                pixmap = QPixmap(str(path))

                # Масштабирование изображения
                max_edge = max(pixmap.width(), pixmap.height())
                if max_edge > 400:
                    if max_edge == pixmap.width():
                        pixmap = pixmap.scaledToWidth(400)
                    else:
                        pixmap = pixmap.scaledToHeight(400)

                img.thumbnail((pixmap.width(), pixmap.height()))

                self.ui.image.resize(pixmap.width(),
                                 pixmap.height())
                self.ui.modifiedImage.resize(pixmap.width(),
                                 pixmap.height())
                self.ui.image.setPixmap(pixmap)
                self.ui.modifiedImage.setPixmap(pixmap)

                image = self.qimage_to_cv2(self.ui.image.pixmap().toImage())
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                threshold_value = 127
                _, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

                height, width = image.shape
                self.ui.modifiedImage.setPixmap(QPixmap.fromImage(QImage(binary_image.data, width, height, width, QImage.Format.Format_Grayscale8)))

                self.ui.erode.clicked.connect(self.erode)
                self.ui.dilate.clicked.connect(self.dilate)
                self.ui.open.clicked.connect(self.open)
                self.ui.close.clicked.connect(self.close)
                self.ui.gradient.clicked.connect(self.gradient)
                self.ui.blackHat.clicked.connect(self.black_hat)


    def erode(self):
        kernel = np.ones((self.ui.kernelWidth.value(), self.ui.kernelHeight.value()), np.uint8)  # Например, квадратное ядро размером 5x5

        image = self.qimage_to_cv2(self.ui.modifiedImage.pixmap().toImage())

        eroded_image = cv2.erode(image, kernel, iterations=1)

        cv2.imshow('Eroded Image', eroded_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def dilate(self):
        kernel = np.ones((self.ui.kernelWidth.value(), self.ui.kernelHeight.value()), np.uint8)  # Например, квадратное ядро размером 5x5

        image = self.qimage_to_cv2(self.ui.modifiedImage.pixmap().toImage())
        dilated_image = cv2.dilate(image, kernel, iterations=1)

        cv2.imshow('Dilated image', dilated_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def close(self):
        kernel = np.ones((self.ui.kernelWidth.value(), self.ui.kernelHeight.value()),
                         np.uint8)  # Например, квадратное ядро размером 5x5

        image = self.qimage_to_cv2(self.ui.modifiedImage.pixmap().toImage())

        closed_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

        cv2.imshow('Closed Image', closed_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def open(self):
        kernel = np.ones((self.ui.kernelWidth.value(), self.ui.kernelHeight.value()),
                         np.uint8)  # Например, квадратное ядро размером 5x5

        image = self.qimage_to_cv2(self.ui.modifiedImage.pixmap().toImage())

        open_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

        cv2.imshow('Open Image', open_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def gradient(self):
        kernel = np.ones((self.ui.kernelWidth.value(), self.ui.kernelHeight.value()),
                         np.uint8)  # Например, квадратное ядро размером 5x5

        image = self.qimage_to_cv2(self.ui.modifiedImage.pixmap().toImage())
        gradient_image = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)

        cv2.imshow('Gradient Image', gradient_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def black_hat(self):
        kernel = np.ones((self.ui.kernelWidth.value(), self.ui.kernelHeight.value()),
                         np.uint8)  # Например, квадратное ядро размером 5x5

        image = self.qimage_to_cv2(self.ui.modifiedImage.pixmap().toImage())
        blackhat_image = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)

        cv2.imshow('Black Hat Image', blackhat_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def qimage_to_cv2(self, qimage):
        byte_array = QByteArray()
        buffer = QBuffer(byte_array)
        buffer.open(QIODeviceBase.OpenModeFlag.ReadWrite)
        qimage.save(buffer, "PNG")  # Save QImage to buffer as PNG format
        buffer.seek(0)  # Move buffer position to the beginning
        img_bytes = buffer.data()  # Get byte array data
        buffer.close()  # Close the buffer

        # Convert byte array to numpy array
        arr = np.asarray(byte_array)

        # Decode PNG formatted image using OpenCV
        cv_image = cv2.imdecode(arr, cv2.IMREAD_UNCHANGED)

        return cv_image


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Form()
    sys.exit(app.exec())




