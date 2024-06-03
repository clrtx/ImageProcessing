import locale
import sys
from io import BytesIO
from pathlib import Path

import PIL
import cv2
import numpy as np
from PIL import Image
from PyQt6.QtCore import QByteArray, QBuffer, QIODevice, QIODeviceBase, QUrl
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QVBoxLayout
from matplotlib import pyplot as plt

from Lab5.app import Ui_Form


class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.file_browse.clicked.connect(self.open_file_dialog)

        # show the login window
        self.show()

        self.openButton = QPushButton("Open Video")
        self.openButton.clicked.connect(self.openFile)

        self.ui.MOG2.clicked.connect(lambda: self.background_subtraction('MOG2'))
        self.ui.KNN.clicked.connect(lambda: self.background_subtraction('KNN'))
        self.ui.motionBlur.clicked.connect(self.blur_moving_objects)

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

                self.ui.Harris.clicked.connect(lambda: self.harris_corner_detection(image))
                self.ui.SIFT.clicked.connect(lambda: self.sift_keypoints(image))
                self.ui.SURF.clicked.connect(lambda: self.surf_keypoints(image))
                self.ui.FAST.clicked.connect(lambda: self.fast_keypoints(image))


    def openFile(self):
        self.fileName, _ = QFileDialog.getOpenFileName(self, "Open Video")





    def background_subtraction(self, input):
        self.openFile()
        # Создаем объект для чтения видео
        cap = cv2.VideoCapture(self.fileName)


        if input is 'KNN':
            backSub = cv2.createBackgroundSubtractorKNN()

        else:
            backSub = cv2.createBackgroundSubtractorMOG2()


        while True:
            # Читаем кадр из видео
            ret, frame = cap.read()
            if not ret:
                break

            # Применяем вычитание фона
            fg_mask = backSub.apply(frame)

            # Отображаем оригинальный кадр и маску переднего плана
            cv2.imshow('Frame', frame)
            cv2.imshow(input, fg_mask)

            # Выход по нажатию клавиши 'q'
            if cv2.waitKey(30) & 0xFF == ord('q'):
                break

        # Освобождаем объект захвата видео и закрываем все окна
        cap.release()
        cv2.destroyAllWindows()

    def blur_moving_objects(self, blur_strength=15):
        self.openFile()

        # Создаем объект для чтения видео
        capture = cv2.VideoCapture(self.fileName)

        # Инициализируем алгоритм для вычитания фона
        ret, frame = capture.read()
        motion_blur_frame = np.zeros_like(frame, dtype=np.float32)
        alpha = 0.2  # Коэффициент смешивания

        while True:
            ret, frame = capture.read()
            if not ret:
                break

            # Обновление накопленного изображения с движением
            cv2.accumulateWeighted(frame, motion_blur_frame, alpha)
            blurred_frame = cv2.convertScaleAbs(motion_blur_frame)

            # Отображение результатов
            cv2.imshow('Frame', frame)
            cv2.imshow('Motion Blur Frame', blurred_frame)

            if cv2.waitKey(30) & 0xFF == ord('q'):
                break

        capture.release()
        cv2.destroyAllWindows()

    def harris_corner_detection(self, image, block_size=2, ksize=3, k=0.04):
        # Преобразуйте изображение в оттенки серого
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray_image = np.float32(gray_image)

        # Примените детектор углов Харриса
        dst = cv2.cornerHarris(gray_image, block_size, ksize, k)

        # Расширьте области углов для лучшего отображения
        dst = cv2.dilate(dst, None)

        # Пороговое значение для определения углов
        threshold = 0.01 * dst.max()
        image[dst > threshold] = [0, 0, 0]  # Отметить углы красным цветом

        cv2.imshow('Harris detector', image)


    def sift_keypoints(self, image):
        # Преобразуйте изображение в оттенки серого
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Инициализируйте SIFT детектор
        sift = cv2.SIFT_create()

        # Найдите ключевые точки и дескрипторы
        keypoints, descriptors = sift.detectAndCompute(gray_image, None)

        # Нарисуйте ключевые точки на изображении
        output_image = cv2.drawKeypoints(image, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        cv2.imshow('SIFT detector', output_image)

    def surf_keypoints(self, image, hessian_threshold=400):
        # Преобразуйте изображение в оттенки серого
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Инициализируйте SURF детектор
        surf = cv2.SURF_create(hessian_threshold)

        # Найдите ключевые точки и дескрипторы
        keypoints, descriptors = surf.detectAndCompute(gray_image, None)

        # Нарисуйте ключевые точки на изображении
        output_image = cv2.drawKeypoints(image, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        cv2.imshow('SURF detector', output_image)

    def fast_keypoints(self, image):

        # Преобразуйте изображение в оттенки серого
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Инициализируйте FAST детектор
        fast = cv2.FastFeatureDetector_create()

        # Найдите ключевые точки
        keypoints = fast.detect(gray_image, None)

        # Нарисуйте ключевые точки на изображении
        output_image = cv2.drawKeypoints(image, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        cv2.imshow('FAST detector', output_image)


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




