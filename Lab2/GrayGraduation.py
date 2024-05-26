from statistics import mean


class GrayGraduation:
    def convert(self, rgb):
        return round((rgb[0] * 0.299 + rgb[1] * 0.587 + rgb[2] * 0.114))
