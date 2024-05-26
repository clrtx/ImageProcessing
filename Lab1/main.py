import locale
import os
import sys
import time
from pathlib import Path

import PIL
from PIL import Image
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog

from Lab1.Converter import Converter
from Lab1.app import Ui_Form


class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.converter = Converter()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.calculate_models(self.ui.r_rgb)

        self.ui.file_browse.clicked.connect(self.open_file_dialog)

        self.connect(self.ui.r_rgb)
        self.connect(self.ui.g_rgb)
        self.connect(self.ui.b_rgb)

        self.connect(self.ui.c_cmyk)
        self.connect(self.ui.m_cmyk)
        self.connect(self.ui.y_cmyk)
        self.connect(self.ui.k_cmyk)

        self.connect(self.ui.h_hsl)
        self.connect(self.ui.s_hsl)
        self.connect(self.ui.l_hsl)

        self.connect(self.ui.l_lab)
        self.connect(self.ui.a_lab)
        self.connect(self.ui.b_lab)

        self.connect(self.ui.h_hsv)
        self.connect(self.ui.s_hsv)
        self.connect(self.ui.v_hsv)

        self.connect(self.ui.y_ycbcr)
        self.connect(self.ui.cb_ycbcr)
        self.connect(self.ui.cr_ycbcr)

        # show the login window
        self.show()

    def connect(self, input):
        input.editingFinished.connect(lambda: self.calculate_models(input))

    def clear_info(self):
        self.ui.deviceSize.setText('Размер на диске:')
        self.ui.imageSize.setText('Разрешение:')
        self.ui.colorDepth.setText('Глубина цвета:')
        self.ui.format.setText('Формат файла:')
        self.ui.colorModel.setText('Цветовая модель:')
        self.ui.creationDate.setText('Дата создания:')

    def open_file_dialog(self):
        self.clear_info()

        filename, ok = QFileDialog.getOpenFileName(
            self.ui,
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

                # print(datetime.datetime.strptime(time.ctime(os.path.getctime(path)), "%a %b %d %H:%M:%S %Y"))

                pixmap = QPixmap(str(path))
                max_edge = max(pixmap.width(), pixmap.height())

                if max_edge > 400:
                    if max_edge == pixmap.width():
                        pixmap = pixmap.scaledToWidth(400)
                    else:
                        pixmap = pixmap.scaledToHeight(400)

                self.ui.image.resize(pixmap.width(),
                                 pixmap.height())
                self.ui.image.setPixmap(pixmap)

                size = os.path.getsize(filename)
                self.ui.deviceSize.setText(f'{self.ui.deviceSize.text()} {round(size / 1024)} КБ ({size} байт)')
                self.ui.imageSize.setText(f'{self.ui.imageSize.text()} w - {img.size[0]} пикселей, h - {img.size[1]} пикселей')
                self.ui.colorDepth.setText(f'{self.ui.colorDepth.text()} {img.bits} битов')
                self.ui.format.setText(f'{self.ui.format.text()} {img.format}')
                self.ui.colorModel.setText(f'{self.ui.colorModel.text()} {img.mode}')
                self.ui.creationDate.setText(f'{self.ui.creationDate.text()} {time.ctime(os.path.getctime(path))}')

                # ImageHelper.rgb_to_cmyk(img)
                # ImageHelper.rgb_to_lab(img)


    def calculate_models(self, input, exclude = ""):
        try:
            if "rgb" in input.objectName():
                r_rgb, g_rgb, b_rgb = int(self.ui.r_rgb.text()), int(self.ui.g_rgb.text()), int(self.ui.b_rgb.text())

                if r_rgb < 0:
                    r_rgb = 0
                if r_rgb > 255:
                    r_rgb = 255

                if g_rgb < 0:
                    g_rgb = 0
                if g_rgb > 255:
                    g_rgb = 255

                if b_rgb < 0:
                    b_rgb = 0
                if b_rgb > 255:
                    b_rgb = 255

                self.ui.color.setStyleSheet(f"background: rgb({r_rgb}, {g_rgb}, {b_rgb});")


                if "cmyk" not in exclude:
                    c_cmyk, m_cmyk, y_cmyk, k_cmyk = self.converter.rgb_to_cmyk(r_rgb, g_rgb, b_rgb)
                    self.ui.c_cmyk.setText(str(c_cmyk))
                    self.ui.m_cmyk.setText(str(m_cmyk))
                    self.ui.y_cmyk.setText(str(y_cmyk))
                    self.ui.k_cmyk.setText(str(k_cmyk))

                if "hsl" not in exclude:
                    h_hsl, s_hsl, l_hsl = self.converter.rgb_to_hsl(r_rgb, g_rgb, b_rgb)
                    self.ui.h_hsl.setText(str(h_hsl))
                    self.ui.s_hsl.setText(str(s_hsl))
                    self.ui.l_hsl.setText(str(l_hsl))

                if "lab" not in exclude:
                    l_lab, a_lab, b_lab = self.converter.rgb_to_lab(r_rgb, g_rgb, b_rgb)
                    self.ui.l_lab.setText(str(l_lab))
                    self.ui.a_lab.setText(str(a_lab))
                    self.ui.b_lab.setText(str(b_lab))

                if "hsv" not in exclude:
                    h_hsv, s_hsv, v_hsv = self.converter.rgb_to_hsv(r_rgb, g_rgb, b_rgb)
                    self.ui.h_hsv.setText(str(h_hsv))
                    self.ui.s_hsv.setText(str(s_hsv))
                    self.ui.v_hsv.setText(str(v_hsv))

                if "ycbcr" not in exclude:
                    y_ycbcr, cb_ycbcr, cr_ycbcr = self.converter.rgb_to_ycbcr(r_rgb, g_rgb, b_rgb)
                    self.ui.y_ycbcr.setText(str(y_ycbcr))
                    self.ui.cb_ycbcr.setText(str(cb_ycbcr))
                    self.ui.cr_ycbcr.setText(str(cr_ycbcr))


            else:
                r, g, b = 0, 0, 0

                exclude = ""
                if "cmyk" in input.objectName():
                    r, g, b = self.converter.cmyk_to_rgb(int(self.ui.c_cmyk.text()) / 100, int(self.ui.m_cmyk.text()) / 100,
                                               int(self.ui.y_cmyk.text()) / 100,
                                               int(self.ui.k_cmyk.text()) / 100, )
                    exclude = "cmyk"
                if "hsl" in input.objectName():
                    r, g, b = self.converter.hsl_to_rgb(int(self.ui.h_hsl.text()), int(self.ui.s_hsl.text()) / 100,
                                               int(self.ui.l_hsl.text()) / 100)
                    exclude = "hsl"

                if "lab" in input.objectName():
                    r, g, b = self.converter.lab_to_rgb(int(self.ui.l_lab.text()), int(self.ui.a_lab.text()),
                                                        int(self.ui.b_lab.text()))
                    exclude = "lab"

                if "hsv" in input.objectName():
                    r, g, b = self.converter.hsv_to_rgb(int(self.ui.h_hsv.text()), int(self.ui.s_hsv.text()) / 100,
                                               int(self.ui.v_hsv.text()) / 100)
                    exclude = "hsv"

                if "ycbcr" in input.objectName():
                    r, g, b = self.converter.ycbcr_to_rgb(int(self.ui.y_ycbcr.text()), int(self.ui.cb_ycbcr.text()),
                                               int(self.ui.cr_ycbcr.text()))
                    exclude = "ycbcr"

                self.ui.r_rgb.setText(str(r))
                self.ui.g_rgb.setText(str(g))
                self.ui.b_rgb.setText(str(b))

                self.calculate_models(self.ui.r_rgb, exclude)
                return

        except Exception as e:
            print(e)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Form()
    r, g, b = (255, 255, 255)
    converter = Converter()

    print(converter.rgb_to_cmyk(r, g, b))
    print(converter.rgb_to_hsl(r, g, b))
    print(converter.rgb_to_lab(r, g, b))
    print(converter.rgb_to_hsv(r, g, b))
    print(converter.rgb_to_ycbcr(r, g, b))
    print(converter.lab_to_rgb(0, 0, 35))

    sys.exit(app.exec())




