class Converter:
    def set_brightness(self, rgb, brightness_value = 1):
        r, g, b = rgb
        norm_r = r / 255
        norm_g = g / 255
        norm_b = b / 255

        return self.constraint(norm_r * brightness_value), self.constraint(norm_g * brightness_value), self.constraint(norm_b * brightness_value)

    def constraint(self, value):
        res = value * 255

        if res > 255:
            return 255
        return round(res)
