import numpy as np
from PIL import Image, ImageOps

from tile import Tile
from ImageObj import ImageObj
from html_settings import HEADER, FOOTER


class AsciiConverter:
    def __init__(self, input: ImageObj, out: str, style: str):
        self.input = input
        self.out = out
        self.style = style

    def convert(self):
        # 1. open image
        img = Image.open(self.input.input_file)

        # 2. resize image
        resize_img = img.resize(
            (
                self.input.width * 2,
                int(img.height * (self.input.width / img.width)) * 2,
            ),
            Image.BICUBIC,
        )
        self.input.set_color_numpy(self.input.img_to_numpy(resize_img))

        # 3. image to bw image
        self.input.set_bw_img(ImageOps.grayscale(resize_img))
        self.input.set_bw_numpy(np.array(self.input.bw_img))

        # 4. bw image to 4 level gray scale numpy
        self.input.set_grayscale_numpy(
            self.input.to_four_level_numpy(self.input.bw_numpy)
        )

        if self.out == "terminal":
            self.to_terminal()
        elif self.out == "html":
            match self.style:
                case "line":
                    self.to_html(color=False, style="line")
                case "color":
                    self.to_html(color=True, style="default")
                case "bw":
                    self.to_html(color=False, style="default")
                case "emoji":
                    self.to_html(color=False, style="emoji")
                case "test":
                    self.to_html(color=True, style="test")

    def to_terminal(self):
        for row_num, row in enumerate(self.input.grayscale_numpy):
            if row_num % 2 == 1:
                pass
            else:
                for col_num, element in enumerate(row):
                    if col_num % 2 == 1:
                        pass
                    else:
                        row1_col1 = element
                        row1_col2 = row[col_num + 1]
                        row2_col1 = self.input.grayscale_numpy[row_num + 1][col_num]
                        row2_col2 = self.input.grayscale_numpy[row_num + 1][col_num + 1]
                        tile = Tile([row1_col1, row1_col2, row2_col1, row2_col2])
                        tile.convert_to_terminal()
                print("")

    def to_html(self, color, style):
        html_file = open("result/" + style + ".html", "w")
        html_file.write(HEADER)

        # tiling
        for row_num, row in enumerate(self.input.grayscale_numpy):
            if row_num % 2 != 1:
                for col_num, element in enumerate(row):
                    if col_num % 2 != 1:
                        row1_col1 = element
                        row1_col2 = row[col_num + 1]
                        row2_col1 = self.input.grayscale_numpy[row_num + 1][col_num]
                        row2_col2 = self.input.grayscale_numpy[row_num + 1][col_num + 1]
                        input_array = [row1_col1, row1_col2, row2_col1, row2_col2]
                        tile = Tile(input_array)

                        # color
                        if color:
                            match style:
                                case "default":
                                    alphabet = tile.convert_to_char(style)
                                case "test":
                                    alphabet = tile.convert_to_char(style)

                            color_array = [
                                self.input.color_numpy[row_num][col_num],
                                self.input.color_numpy[row_num][col_num + 1],
                                self.input.color_numpy[row_num + 1][col_num],
                                self.input.color_numpy[row_num + 1][col_num + 1],
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

                        # black and white
                        else:
                            match style:
                                case "default":
                                    alphabet = tile.convert_to_char(style)
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
                                    alphabet = tile.convert_to_char(style)
                                    html_file.write("<span>" + alphabet + "</span>")
                                case "emoji":
                                    alphabet = tile.convert_to_char(style)
                                    html_file.write("<span>&#" + alphabet + "</span>")

                html_file.write("<br />\n")

        html_file.write(FOOTER)
        html_file.close()
