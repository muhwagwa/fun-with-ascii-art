import numpy as np
from PIL import Image


class ImageObj:
    def __init__(self, input_file, width):
        self.input_file = input_file
        self.width = width

    def set_input_numpy(self):
        self.input_numpy = Image.fromarray(self.input_file.astype(np.uint8))

    def set_color_numpy(self, color_numpy):
        self.color_numpy = color_numpy

    def set_bw_img(self, bw_img):
        self.bw_img = bw_img

    def set_bw_numpy(self, bw_numpy):
        self.bw_numpy = bw_numpy

    def set_grayscale_img(self, grayscale_img):
        self.grayscale_img = grayscale_img

    def set_grayscale_numpy(self, grayscale_numpy):
        self.grayscale_numpy = grayscale_numpy

    def set_check_array(self, check_array):
        self.check_array = check_array

    def set_ascii(self, ascii):
        self.ascii = ascii

    def save_img(self, img):
        img.save("ascii.jpg")

    def img_to_numpy(self, img):
        return np.array(img)

    def numpy_to_img(self, numpy_array):
        return Image.fromarray(numpy_array.astype(np.uint8))

    def to_four_level_numpy(self, bw_numpy):
        four_level_array = []
        q1 = np.quantile(bw_numpy, 0.15)
        q2 = np.quantile(bw_numpy, 0.35)
        q3 = np.quantile(bw_numpy, 0.75)
        for row in bw_numpy:
            tmp_row = []
            for block in row:
                if block <= q1:
                    tmp_row.append(0)
                elif block > q1 and block <= q2:
                    tmp_row.append(70)
                if block > q2 and block <= q3:
                    tmp_row.append(140)
                if block > q3:
                    tmp_row.append(210)
            four_level_array.append(tmp_row)

        four_level_numpy = np.array(four_level_array)
        return four_level_numpy

    def show_img(self, img):
        img.show()
