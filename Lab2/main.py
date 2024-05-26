import locale
import os
import sys
import time
from pathlib import Path

import PIL
from PIL import Image
from PyQt6.QtGui import QPixmap, QImage, QColor
from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog

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
                # self.label.setBaseSize(img.size)
                locale.setlocale(locale.LC_TIME, "ru_RU")
                img = img.convert('L')

                pixmap = QPixmap(str(path))
                max_edge = max(pixmap.width(), pixmap.height())

                if max_edge > 400:
                    if max_edge == pixmap.width():
                        pixmap = pixmap.scaledToWidth(400)
                    else:
                        pixmap = pixmap.scaledToHeight(400)

                img.thumbnail((pixmap.width(), pixmap.height()))

                self.ui.image.resize(img.width,
                                 img.height)
                self.ui.image.setPixmap(pixmap)


                grayImage = QImage(self.ui.image.width(), self.ui.image.height(), QImage.Format.Format_Grayscale8)
                image = QImage(self.ui.image.width(), self.ui.image.height(), QImage.Format.Format_RGB32)

                for i in range(self.ui.image.width()):
                    for j in range(self.ui.image.height()):
                        grayImage.setPixel(i, j, self.grayGraduation.convert(img.getpixel((i, j))))

                for i in range(self.ui.image.width()):
                    for j in range(self.ui.image.height()):
                        r, g, b = self.converter.set_brightness(img.getpixel((i, j)), 2000.1)
                        image.setPixelColor(i, j, QColor.fromRgb(r, g, b))

                pixmap = QPixmap.fromImage(image)
                self.ui.image.setPixmap(pixmap)

                grayPixmap = QPixmap().fromImage(grayImage)
                self.ui.grayImage.resize(pixmap.width(),
                                 pixmap.height())
                self.ui.grayImage.setPixmap(grayPixmap)



if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Form()
    sys.exit(app.exec())




