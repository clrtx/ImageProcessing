from PIL import Image, ImageEnhance
from PyQt6.QtGui import QImage


class Converter:
    def set_contrast(self, im, factor):
        enhancer = ImageEnhance.Contrast(im)
        im_output = enhancer.enhance(factor)
        return im_output

    def set_brightness(self, im, factor):
        enhancer = ImageEnhance.Brightness(im)
        im_output = enhancer.enhance(factor)
        return im_output

    def set_color(self, im, factor):
        enhancer = ImageEnhance.Color(im)
        im_output = enhancer.enhance(factor)
        return im_output

    def pil_image_to_qimage(self, pil_image):
        # Преобразуем изображение PIL в формат RGBA, если оно еще не в этом формате
        if pil_image.mode != 'RGBA':
            pil_image = pil_image.convert('RGBA')

        # Получаем данные изображения PIL в виде байтового массива
        data = pil_image.tobytes('raw', 'RGBA')

        # Создаем QImage из байтового массива
        qimage = QImage(data, pil_image.width, pil_image.height, QImage.Format.Format_RGBA8888)

        return qimage