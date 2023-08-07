"""Tile
2x2 Tile object that will be converted to 1 ascii char.

This file can also be imported as a module and contains the following functions:

    * create_check_array : Create an array that holds shape info for a 2x2 tile
    * print_terminal : Print alphabet to terminal with matching color
    * convert_to_char : Convert 2x2 tile info to ascii char
"""
from colorama import Fore, Style
import tables


class Tile:
    """2x2 Tile object that will be converted to 1 ascii char.

    Attributes:
        input_array (list): List of initial cell values.
        color_array (list): List of rgb values of the cells in the tile.
        check (list): List of binary cell values.
        count (list): No. of cells each with value 0, 70, 140 and 210.
        max_frequency (int): Maximum frequency of the cell values in a tile.
        chosen (int): Cell value with maximum frequency.
    """

    def __init__(self, input_array: list):
        self.input_array = input_array
        self.color_array = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.check = [0, 0, 0, 0]
        self.count = [0, 0, 0, 0]
        self.max_frequency = 0
        self.chosen = 0

    def create_check_array(self):
        """Create an array that holds shape info for a 2x2 tile"""
        for elem in self.input_array:
            self.count[int(elem / 70)] += 1

        self.max_frequency = max(self.count)
        max_index = self.count.index(self.max_frequency)
        self.chosen = 70 * max_index

        for index, elem in enumerate(self.input_array):
            if elem == self.chosen:
                self.check[index] = 1

    def print_terminal(self, alphabet: str):
        """Print alphabet to terminal with matching color

        Args:
            alphabet (str): Alphabet to print to terminal
        """
        match self.chosen:
            case 0:
                print(Fore.BLACK + Style.NORMAL + alphabet, end=" ")
            case 70:
                print(Fore.BLACK + Style.BRIGHT + alphabet, end=" ")
            case 140:
                print(Fore.WHITE + Style.NORMAL + alphabet, end=" ")
            case 210:
                print(Fore.WHITE + Style.BRIGHT + alphabet, end=" ")
        print(Style.RESET_ALL, end="")

    def convert_to_char(self, style: str):
        """Convert 2x2 tile info to ascii char

        Args:
            style (str): Desired style of Ascii converting.

        Returns:
            str: result ascii char of the tile
        """
        self.create_check_array()
        match style:
            case "terminal":
                alphabet = tables.default(self.check)
                self.print_terminal(alphabet)
            case "bw":
                return tables.default(self.check)
            case "color":
                return tables.default(self.check)
            case "line":
                return tables.line(self.check)
            case "underscore":
                return tables.line2(self.check)
            case "korean":
                return tables.korean(self.check)
            case "emoji":
                return tables.emoji(self.check)
