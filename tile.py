from colorama import Fore, Style
import tables


class Tile:
    def __init__(self, input_array):
        self.input_array = input_array
        self.color_array = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.check = [0, 0, 0, 0]
        self.count0 = 0
        self.count70 = 0
        self.count140 = 0
        self.count210 = 0
        self.max_frequency = 0
        self.chosen = 0

    def create_check_array(self):
        for elem in self.input_array:
            match elem:
                case 0:
                    self.count0 += 1
                case 70:
                    self.count70 += 1
                case 140:
                    self.count140 += 1
                case 210:
                    self.count210 += 1

        self.max_frequency = max(
            self.count0, self.count70, self.count140, self.count210
        )

        if self.count0 == self.max_frequency:
            self.chosen = 0
        elif self.count70 == self.max_frequency:
            self.chosen = 70
        elif self.count140 == self.max_frequency:
            self.chosen = 140
        elif self.count210 == self.max_frequency:
            self.chosen = 210

        for index, elem in enumerate(self.input_array):
            if elem == self.chosen:
                self.check[index] = 1

    def print_terminal(self, alphabet):
        match self.chosen:
            case 0:
                print(Fore.BLACK + Style.NORMAL + alphabet, end="")
                print(Style.RESET_ALL, end="")
            case 70:
                print(Fore.BLACK + Style.BRIGHT + alphabet, end="")
                print(Style.RESET_ALL, end="")
            case 140:
                print(Fore.WHITE + Style.NORMAL + alphabet, end="")
                print(Style.RESET_ALL, end="")
            case 210:
                print(Fore.WHITE + Style.BRIGHT + alphabet, end="")
                print(Style.RESET_ALL, end="")

    def convert_to_terminal(self):
        self.create_check_array()
        alphabet = tables.default(self.check)
        self.print_terminal(alphabet)

    def convert_to_char(self, style):
        self.create_check_array()
        match style:
            case "terminal":
                alphabet = tables.default(self.check)
                self.print_terminal(alphabet)
            case "bw":
                return tables.default(self.check)
            case "color":
                return tables.default(self.check)
            case "test":
                return tables.test(self.check)
            case "line":
                return tables.line(self.check)
            case "emoji":
                return tables.emoji(self.check)
