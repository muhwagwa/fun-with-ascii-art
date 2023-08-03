import numpy as np


class ImageObj:
    def __init__(self, input_file, width):
        self.input_file = input_file
        self.width = width

    def set_color_numpy(self, color_numpy):
        self.color_numpy = color_numpy

    def set_bw_img(self, bw_img):
        self.bw_img = bw_img

    def set_bw_numpy(self, bw_numpy):
        self.bw_numpy = bw_numpy

    def set_grayscale_numpy(self, grayscale_numpy):
        self.grayscale_numpy = grayscale_numpy

    def img_to_numpy(self, img):
        return np.array(img)

    def to_four_level_numpy(self, bw_numpy):
        four_level_array = []
        q_1 = np.quantile(bw_numpy, 0.15)
        q_2 = np.quantile(bw_numpy, 0.35)
        q_3 = np.quantile(bw_numpy, 0.75)
        for row in bw_numpy:
            tmp_row = []
            for block in row:
                if block <= q_1:
                    tmp_row.append(0)
                elif block <= q_2:
                    tmp_row.append(70)
                if block > q_2 and block <= q_3:
                    tmp_row.append(140)
                if block > q_3:
                    tmp_row.append(210)
            four_level_array.append(tmp_row)

        four_level_numpy = np.array(four_level_array)
        return four_level_numpy
