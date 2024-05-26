class Converter:
    def cast(self, x):
        return round(x * 100)

    def rgb_to_cmyk(self, red, green, blue):
        # Переводим RGB в диапазоне [0, 255] в процентный диапазон [0, 1]
        r = red / 255
        g = green / 255
        b = blue / 255



        # Находим минимальное значение из CMY
        k = 1 - max(r, g, b)

        # Если K равно нулю, все остальные компоненты также равны нулю
        if k == 1:
            return 0, 0, 0, 1

        # Вычисляем оставшиеся компоненты CMY
        c = (1 - r - k) / (1 - k)
        m = (1 - g - k) / (1 - k)
        y = (1 - b - k) / (1 - k)

        return round(c * 100), round(m * 100), round(y * 100), round(k * 100)

    def rgb_to_hsl(self, red, green, blue):
        # Переводим RGB в диапазоне [0, 255] в процентный диапазон [0, 1]
        r = red / 255
        g = green / 255
        b = blue / 255

        max_color_value = max(r, g, b)
        min_color_value = min(r, g, b)
        delta = max_color_value - min_color_value

        l = 0

        # Черный или белый цвет
        if delta == 0:
            h = 0
            l = (max_color_value + min_color_value) / 2
            s = 0
            return round(h), round(s), round(l * 100)

        # Hue (тон)
        if max_color_value == r:
            h = ((g - b) / delta) % 6
        elif max_color_value == g:
            h = (b - r) / delta + 2
        elif max_color_value == b:
            h = (r - g) / delta + 4

        h = round(h * 60)

        # Lightness (яркость)
        l = (max_color_value + min_color_value) / 2

        # Saturation (насыщенность)
        if delta == 0:
            s = 0
        else:
            s = delta / (1 - abs(2 * l - 1))

        return round(h), round(s * 100), round(l * 100)

    def norm(self, t):
        return ((t + 0.055) / 1.055) ** 2.4 if t > 0.045045 else t / 12.92

    def rgb_to_lab(self, r, g, b):
        r, g, b = [x / 255. for x in [r, g, b]]

        var_r, var_g, var_b = 100 * self.norm(r), 100* self.norm(g), 100 * self.norm(b),

        # Преобразование из RGB в XYZ
        x = (var_r * 0.412453 + var_g * 0.357580 + var_b * 0.180423)
        y = (var_r * 0.212671 + var_g * 0.715160 + var_b * 0.072169)
        z = (var_r * 0.019334 + var_g * 0.119193 + var_b * 0.950227)

        ref_x = 95.047
        ref_y = 100.000
        ref_z = 108.883

        # x = 4.950280289802328
        # y = 4.415476751814342
        # z = 27.025186241611866

        x /= ref_x
        y /= ref_y
        z /= ref_z



        # Преобразование из XYZ в LAB
        l = 116 * self.f_xyz(y) - 16
        a = 500 * (self.f_xyz(x) - self.f_xyz(y))
        b = 200 * (self.f_xyz(y) - self.f_xyz(z))

        # return x, y, z
        return round(l), round(a), round(b)

    def f_xyz(self, t):
        return t ** (1/3) if t > 0.008856 else 7.787*t + 16.0/116.0

    def rgb_to_hsv(self, r, g, b):
        # Нормализация значений RGB
        r, g, b = [x / 255. for x in [r, g, b]]

        # Нахождение минимального и максимального значений
        min_val = min(r, g, b)
        max_val = max(r, g, b)

        delta = max_val - min_val
        # Вычисление насыщенности и яркости
        s = delta/max_val if max_val != 0 else 0

        h = 0
        # Вычисление тона
        if max_val == min_val:
            h = 0.0
        elif max_val == r:
            h = (((g - b) / delta) % 6)
        elif max_val == g:
            h = ((b - r) / delta + 2)
        elif max_val == b:
            h = (r - g) / delta + 4
        h *= 60

        return round(h), round(s * 100), round(max_val * 100)

    def rgb_to_ycbcr(self, red, green, blue):
        # red, green, blue = [x / 255. for x in [red, green, blue]]

        # Матрица преобразования из RGB в YCbCr
        y_offset = 16
        u_offset = 128
        v_offset = 128

        # Преобразование компонентов RGB в Y', Cb и Cr
        y_prime = round((0.257 * red) + (0.504 * green) + (0.098 * blue)) + y_offset
        cb = round((-0.148 * red) - (0.291 * green) + (0.439 * blue)) + u_offset
        cr = round((0.439 * red) - (0.368 * green) - (0.071 * blue)) + v_offset

        return round(y_prime), round(cb), round(cr)

    def cmyk_to_rgb(self, c, m, y, k):
        r = 255 * (1 - c) * (1 - k)
        g = 255 * (1 - m) * (1 - k)
        b = 255 * (1 - y) * (1 - k)

        return round(r), round(g), round(b)

    def hsl_to_rgb(self, h, s, l):

        c = (1 - abs(2 * l - 1)) * s
        x = c * (1 - abs((h / 60) % 2 - 1))
        m = l - c / 2

        _r, _g, _b = 0, 0, 0

        if h < 60:
            _r = c
            _g = x
            _b = 0
        elif 60 <= h < 120:
            _r = x
            _g = c
            _b = 0
        elif 120 <= h < 180:
            _r = 0
            _g = c
            _b = x
        elif 180 <= h < 240:
            _r = 0
            _g = x
            _b = c
        elif 240 <= h < 300:
            _r = x
            _g = 0
            _b = c
        elif 300 <= h < 360:
            _r = c
            _g = 0
            _b = x

        return round((_r + m) * 255), round((_g + m) * 255), round((_b + m) * 255)

    def hsv_to_rgb(self, h, s, v):
        c = v * s
        x = c * (1 - abs((h / 60) % 2 - 1))
        m = h - c

        _r, _g, _b = 0, 0, 0

        if h < 60:
            _r = c
            _g = x
            _b = 0
        elif 60 <= h < 120:
            _r = x
            _g = c
            _b = 0
        elif 120 <= h < 180:
            _r = 0
            _g = c
            _b = x
        elif 180 <= h < 240:
            _r = 0
            _g = x
            _b = c
        elif 240 <= h < 300:
            _r = x
            _g = 0
            _b = c
        elif 300 <= h < 360:
            _r = c
            _g = 0
            _b = x

        return round((_r + m) * 255), round((_g + m) * 255), round((_b + m) * 255)

    def ycbcr_to_rgb(self, y, cb, cr):
        r = y + 1.40200 * (cr - 128)
        g = y - 0.34414 * (cb - 128) - 0.71414 * (cr - 128)
        b = y + 1.77200 * (cb - 128)

        return round(r), round(g), round(b)

    def lab_to_rgb(self, l, a, b):
        # lab to xyz
        var_Y = (l + 16) / 116
        var_X = a / 500 + var_Y
        var_Z = var_Y - b / 200

        var_X = self.var(var_X)
        var_Y = self.var(var_Y)
        var_Z = self.var(var_Z)

        ref_x = 95.047
        ref_y = 100.000
        ref_z = 108.883

        x = var_X * ref_x
        y = var_Y * ref_y
        z = var_Z * ref_z

        # xyz to rgb
        var_x = x / 100
        var_y = y / 100
        var_z = z / 100

        var_r = self.var_rgb(var_x * 3.2406 + var_y * -1.5372 + var_z * -0.4986)
        var_g = self.var_rgb(var_x * -0.9689 + var_y * 1.8758 + var_z * 0.0415)
        var_b = self.var_rgb(var_x * 0.0557 + var_y * -0.2040 + var_z * 1.0570)

        return round(var_r * 255), round(var_g * 255), round(var_b * 255)

    def var(self, t):
        return t ** 3 if t ** 3 > 0.008856 else (t - 16 / 116) / 7.787

    def var_rgb(self, t):
        return 1.055 * (t ** (1 / 2.4)) - 0.055 if t > 0.0031308 else t * 12.92