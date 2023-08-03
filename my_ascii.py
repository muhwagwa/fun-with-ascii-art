import argparse
import os
from ImageObj import ImageObj
from AsciiConverter import AsciiConverter
from helper import png_to_jpg, check_file_extension


def convert_img(img_file):
    if img_file.endswith(".png"):
        img_file = png_to_jpg(img_file)
    if not check_file_extension(img_file):
        print(img_file + " is not an image file")
        return

    img = ImageObj(img_file, int(args.width))
    converter = AsciiConverter(img, args.out, args.style)
    converter.convert()


if __name__ == "__main__":
    # create an arg parser
    DESCRIPTION = "Image to ASCII Art Converter"
    parser = argparse.ArgumentParser(description=DESCRIPTION)

    parser.add_argument("--file", dest="img_file", required=True)
    parser.add_argument("--width", dest="width", required=True)
    parser.add_argument(
        "--style",
        dest="style",
        required=True,
        choices=["bw", "color", "emoji", "line", "test", "four", "replace"],
    )
    parser.add_argument(
        "--out", dest="out", required=True, choices=["html", "terminal"]
    )

    args = parser.parse_args()

    # if img_file is a file
    if os.path.isfile(args.img_file):
        convert_img(args.img_file)
    # if img_file is a directory
    else:
        files = os.listdir(args.img_file)
        files.sort()
        for file in files:
            filename = args.img_file + "/" + file
            print(filename)
            convert_img(filename)
