"""Ascii Converter
Converts an image to Ascii format.

This file can also be imported as a module and contains the following functions:

    * convert : Preprocess the image and then output the ascii version
    * write_ascii : Writes the result ascii to terminal or an html file
"""
import numpy as np
from PIL import Image, ImageOps

from tile import Tile
from ImageObj import ImageObj
from constants import HEADER, FOOTER


class AsciiConverter:
    """Converts an image file to Ascii

    Attributes:
        input_img (ImageObj): Image file to convert.
        out (str): Desired format of the output file.
        style (str): Desired style of Ascii converting.
        out_dir (str): Path to put the output file.
    """

    def __init__(self, input_img: ImageObj, out: str, style: str, out_dir: str):
        self.input_img = input_img
        self.out = out
        self.style = style
        self.out_dir = out_dir

    def convert(self):
        """Preprocess the image and then output the ascii version"""
        # 1. open image
        img = Image.open(self.input_img.input_file)

        # 2. resize image
        resize_img = img.resize(
            (
                self.input_img.width * 2,
                int(img.height * (self.input_img.width / img.width)) * 2,
            ),
            Image.BICUBIC,
        )
        self.input_img.set_color_numpy(self.input_img.img_to_numpy(resize_img))

        # 3. image to bw image
        self.input_img.set_bw_img(ImageOps.grayscale(resize_img))
        self.input_img.set_bw_numpy(np.array(self.input_img.bw_img))

        # 4. bw image to 4 level gray scale numpy
        self.input_img.set_grayscale_numpy(
            self.input_img.to_four_level_numpy(self.input_img.bw_numpy)
        )

        self.write_ascii(self.style, self.out)

    def write_ascii(self, style, out):
        """Writes the result ascii to terminal or an html file

        Args:
            style (str): Desired style of Ascii converting.
            out (str): Desired format of the output file.
        """

        def write_html_line():
            match style:
                case "bw":
                    html_file.write(
                        '<span style="color: rgb('
                        + str(tile.chosen)
                        + ", "
                        + str(tile.chosen)
                        + ", "
                        + str(tile.chosen)
                        + ');">'
                        + str(alphabet)
                        + "</span>"
                    )
                case "line":
                    html_file.write("<span>" + alphabet + "</span>")
                case "emoji":
                    html_file.write("<span>&#" + alphabet + "</span>")
                case "color":
                    html_file.write(
                        '<span style="color: rgb('
                        + str(color[0])
                        + ", "
                        + str(color[1])
                        + ", "
                        + str(color[2])
                        + ');">'
                        + str(alphabet)
                        + "</span>"
                    )

        if out == "html":
            html_file = open(
                self.out_dir + self.input_img.name + "_" + style + ".html", "w"
            )
            html_file.write(HEADER)

        # tiling
        for row_num, row in enumerate(self.input_img.grayscale_numpy):
            if row_num % 2 != 1:
                for col_num, element in enumerate(row):
                    if col_num % 2 != 1:
                        row1_col1 = element
                        row1_col2 = row[col_num + 1]
                        row2_col1 = self.input_img.grayscale_numpy[row_num + 1][col_num]
                        row2_col2 = self.input_img.grayscale_numpy[row_num + 1][
                            col_num + 1
                        ]
                        input_array = [row1_col1, row1_col2, row2_col1, row2_col2]
                        tile = Tile(input_array)
                        alphabet = tile.convert_to_char(style)

                        if style == "color":
                            color_array = [
                                self.input_img.color_numpy[row_num][col_num],
                                self.input_img.color_numpy[row_num][col_num + 1],
                                self.input_img.color_numpy[row_num + 1][col_num],
                                self.input_img.color_numpy[row_num + 1][col_num + 1],
                            ]

                            tile.color_array = color_array

                            color = [0, 0, 0]
                            for cell_no, tile_check in enumerate(tile.check):
                                if tile_check == 1:
                                    cell = tile.color_array[cell_no]
                                    for index, color_value in enumerate(cell):
                                        # TODO : check if these 2 lines are necessary
                                        if index > 2:
                                            break
                                        color[index] += color_value / tile.max_frequency

                        if out == "html":
                            write_html_line()

                if out == "terminal":
                    print("")
                else:
                    html_file.write("<br />\n")

        if out == "html":
            html_file.write(FOOTER)
            html_file.close()
