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

from Lab4.app import Ui_Form


class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.file_browse.clicked.connect(self.open_file_dialog)

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

                self.ui.image.setPixmap(pixmap)

                image = self.qimage_to_cv2(self.ui.image.pixmap().toImage())

                self.ui.sharpness.clicked.connect(lambda: self.sharpness(image))
                self.ui.motionBlur.clicked.connect(lambda: self.motion_blur(image))
                self.ui.emboss.clicked.connect(lambda: self.emboss(image))
                self.ui.medianFilter.clicked.connect(lambda: self.median_filter(image))
                self.ui.detectorCanny.clicked.connect(lambda: self.canny(image))
                self.ui.operatorRoberts.clicked.connect(lambda: self.roberts(image))

    def sharpness(self, image):
        kernel = np.array([[0, -1, 0],
                          [-1, 5, -1],
                          [0, -1, 0]], dtype=np.float32)

        sharpened_image = cv2.filter2D(image, -1, kernel)
        cv2.imshow('Sharpened image', sharpened_image)

    def motion_blur(self, image):
        kernel_size = int(self.ui.motionBlurValue.value())

        kernel_motion_blur = np.zeros((kernel_size, kernel_size))
        kernel_motion_blur[int((kernel_size - 1) / 2), :] = np.ones(kernel_size)
        kernel_motion_blur = kernel_motion_blur / kernel_size

        blurred_image = cv2.filter2D(image, -1, kernel_motion_blur)

        cv2.imshow('Blurred image', blurred_image)

    def emboss(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        kernel = np.array([[-2, -1, 0],
                           [-1, 1, 1],
                           [0, 1, 2]])

        embossed_image = cv2.filter2D(gray_image, -1, kernel)

        embossed_image = cv2.normalize(embossed_image, None, 0, 255, cv2.NORM_MINMAX)

        cv2.imshow('Embossed image', embossed_image)

    def median_filter(self, image):
        kernel_size = int(self.ui.medianFilterValue.value())

        filtered_image = cv2.medianBlur(image, kernel_size)

        cv2.imshow('Median filter', filtered_image)

    def canny(self, image):
        tresholds = (int(self.ui.cannyFirstTreshold.value()), int(self.ui.cannySecondTreshold.value()))
        lower_threshold = min(tresholds)
        upper_threshold = max(tresholds)

        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 1.4)

        edges = cv2.Canny(blurred_image, lower_threshold, upper_threshold)
        cv2.imshow('Canny edges', edges)

    def roberts(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        kernel_x = np.array([[1, 0], [0, -1]], dtype=np.float32)
        kernel_y = np.array([[0, 1], [-1, 0]], dtype=np.float32)

        # Примените ядра для вычисления градиентов
        gradient_x = cv2.filter2D(gray_image, cv2.CV_32F, kernel_x)
        gradient_y = cv2.filter2D(gray_image, cv2.CV_32F, kernel_y)

        # Рассчитайте величину градиента
        edges = cv2.magnitude(gradient_x, gradient_y)

        # Нормализуйте изображение для отображения
        edges = cv2.convertScaleAbs(edges)

        cv2.imshow('Roberts edges', edges)

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




