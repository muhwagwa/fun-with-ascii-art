"""ImageObj
Image file object used as an input for the AsciiConverter.

This file can also be imported as a module and contains the following functions:

    * __init__ : Convert PNG to JPG and creates/runs a converter
    * set_color_numpy : Set color_numpy var
    * set_bw_img : Set bw_img var
    * set_bw_numpy : Set bw_numpy var
    * set_grayscale_numpy : Set grayscale_numpy var
    * img_to_numpy : Convert an image to numpy
    * to_four_level_numpy : Convert an image to four level numpy
"""
import numpy as np
from PIL import Image


class ImageObj:
    """Image file object used as an input for the AsciiConverter.

    Attributes:
        input_file (str): Path to an image file.
        width (int): Width of the image file.
        name (str): Name of the image file.
        color_numpy (np.array | None): Numpy representation of image file color version.
        bw_numpy (np.array | None): Numpy representation of image file bw version.
        grayscale_numpy (np.array | None): Numpy representation of image file grayscale version.
        bw_img (np.array | None): Bw version of the image file.
    """

    def __init__(self, input_file: str, width: int):
        self.input_file = input_file
        self.width = width
        self.name = input_file.split("/")[-1].split(".")[0]
        self.color_numpy = None
        self.bw_numpy = None
        self.grayscale_numpy = None
        self.bw_img = None

    def set_color_numpy(self, color_numpy: np.array):
        """Set color_numpy var

        Args:
            color_numpy (np.array): Numpy array representing color image
        """
        self.color_numpy = color_numpy

    def set_bw_img(self, bw_img: Image):
        """Set bw_img var

        Args:
            bw_img (Image): Bw image
        """
        self.bw_img = bw_img

    def set_bw_numpy(self, bw_numpy: np.array):
        """Set bw_numpy var

        Args:
            bw_numpy (np.array): Numpy array representing bw image
        """
        self.bw_numpy = bw_numpy

    def set_grayscale_numpy(self, grayscale_numpy: np.array):
        """Set grayscale_numpy var

        Args:
            grayscale_numpy (np.array): Numpy array representing grayscale image
        """
        self.grayscale_numpy = grayscale_numpy

    def img_to_numpy(self, img: Image):
        """Convert an image to numpy

        Args:
            img (Image): Path to an PNG image file

        Returns:
            np.array: numpy format of the image
        """
        return np.array(img)

    def to_four_level_numpy(self, bw_numpy: np.array):
        """Convert an image to four level numpy

        Args:
            bw_numpy (np.array): Numpy array representing bw image

        Returns:
            np.array: converted numpy array
        """
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
                if q_2 < block <= q_3:
                    tmp_row.append(140)
                if block > q_3:
                    tmp_row.append(210)
            four_level_array.append(tmp_row)

        four_level_numpy = np.array(four_level_array)
        return four_level_numpy
