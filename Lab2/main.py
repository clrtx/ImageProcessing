import locale
import sys
from io import BytesIO
from pathlib import Path

import PIL
import numpy as np
from PIL import Image
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog
from matplotlib import pyplot as plt

from Lab2.Converter import Converter
from Lab2.GrayGraduation import GrayGraduation
from Lab2.app import Ui_Form


class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.grayGraduation = GrayGraduation()
        self.converter = Converter()

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
                self.ui.modifiedImage.resize(pixmap.width(),
                                 pixmap.height())
                self.ui.image.setPixmap(pixmap)
                self.ui.modifiedImage.setPixmap(pixmap)

                # Градация серого
                self.grayImg = img.convert('L')
                grayImage = QImage(self.ui.image.width(), self.ui.image.height(), QImage.Format.Format_Grayscale8)

                for i in range(self.ui.image.width()):
                    for j in range(self.ui.image.height()):
                        grayImage.setPixel(i, j, self.grayImg.getpixel((i, j)))

                grayPixmap = QPixmap().fromImage(grayImage)

                self.ui.grayImage.resize(pixmap.width(),
                                 pixmap.height())
                self.ui.grayImage.setPixmap(grayPixmap)


                self.ui.brightnessSlider.valueChanged.connect(self.modify)
                self.ui.colorSlider.valueChanged.connect(self.modify)
                self.ui.contrastSlider.valueChanged.connect(self.modify)

                self.ui.getHistogram.clicked.connect(self.getHistogram)

                self.ui.linearCorrection.clicked.connect(self.linear_correction)
                self.ui.notLinearCorrection.clicked.connect(self.not_linear_correction)


    def getHistogram(self):
        # self.not_linear_correction()
        image_np = np.array(self.modImg)

        r, g, b = image_np[:, :, 0], image_np[:, :, 1], image_np[:, :, 2]

        fig, axs = plt.subplots(4, 1, figsize=(16, 9), sharex=True, sharey=True)

        axs[0].hist(r.ravel(), bins=256, color='red', alpha=1)
        axs[0].set_title('Красный')

        axs[1].hist(g.ravel(), bins=256, color='green', alpha=1)
        axs[1].set_title('Зеленый')

        axs[2].hist(b.ravel(), bins=256, color='blue', alpha=1)
        axs[2].set_title('Синий')

        for ax in axs:
            ax.set_xlim(0, 256)
            ax.set_ylim(0, np.max([np.histogram(r, bins=256)[0].max(),
                                   np.histogram(g, bins=256)[0].max(),
                                   np.histogram(b, bins=256)[0].max()]))

        plt.xlabel('Оттенок канала')
        plt.ylabel('Частота')

        plt.hist(r.ravel(), bins=256, color='red', alpha=0.5, label='Красный')
        plt.hist(g.ravel(), bins=256, color='green', alpha=0.5, label='Зеленый')
        plt.hist(b.ravel(), bins=256, color='blue', alpha=0.5, label='Синий')

        plt.title('Все каналы')
        plt.xlabel('Оттенок канала')
        plt.ylabel('Частота')
        plt.legend()

        fig.suptitle('Гистограмма изображения')
        # self.ui.histogram.setPixmap(QPixmap(self.converter.pil_image_to_qimage(image)))
        plt.show()



    def linear_correction(self): # Преобразуем в градации серого

        # Коэффициенты усиления и смещения
        gain = 1.5  # Увеличиваем контраст
        bias = 50  # Увеличиваем яркость

        # Применяем линейную коррекцию
        corrected_image = self.grayImg.point(lambda p: p * gain + bias)

        # Отображаем или сохраняем скорректированное изображение
        corrected_image.show()
        # corrected_image.save('corrected_image.jpg')

    def not_linear_correction(self):
        # Преобразуем изображение в массив NumPy
        image_np = np.array(self.grayImg)


        # Применяем нелинейную коррекцию (например, логарифмическую)
        gamma = 2.2 # Параметр экспоненциального преобразования



        # Применяем экспоненциальное преобразование ко всем пикселям
        corrected_array = 255 * ((image_np/255) ** gamma)

        # Создаем новое изображение из скорректированного массива
        corrected_image = Image.fromarray(corrected_array.astype(np.uint8))

        # Отображаем или сохраняем скорректированное изображение
        corrected_image.show()
        # corrected_image.save('corrected_image.jpg')

    def modify(self):
        value = self.ui.brightnessSlider.value() / 100
        img = self.converter.set_brightness(self.img, value)
        self.ui.modifiedImage.setPixmap(QPixmap(self.converter.pil_image_to_qimage(img)))
        self.ui.brightnessValue.setText(str(value))

        value = self.ui.colorSlider.value() / 100
        img = self.converter.set_color(img, value)
        self.ui.modifiedImage.setPixmap(QPixmap(self.converter.pil_image_to_qimage(img)))
        self.ui.colorValue.setText(str(value))

        value = self.ui.contrastSlider.value() / 100
        img = self.converter.set_contrast(img, value)
        self.ui.modifiedImage.setPixmap(QPixmap(self.converter.pil_image_to_qimage(img)))
        self.ui.contrastValue.setText(str(value))
        self.modImg = img

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Form()
    sys.exit(app.exec())




