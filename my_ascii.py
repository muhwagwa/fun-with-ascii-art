import argparse
import os
from ImageObj import ImageObj
from AsciiConverter import AsciiConverter
from helper import png_to_jpg, video_to_frames, is_image_file, is_video_file


def convert_img(img_file, width, out, style):
    if img_file.endswith(".png"):
        img_file = png_to_jpg(img_file)
    if not is_image_file(img_file):
        print(img_file + " is not an image file")
        return

    img = ImageObj(img_file, int(width))
    converter = AsciiConverter(img, out, style)
    converter.convert()


def parse_arg():
    # create an arg parser
    DESCRIPTION = "Image to ASCII Art Converter"
    parser = argparse.ArgumentParser(description=DESCRIPTION)

    parser.add_argument("--file", dest="input_file", required=True)
    parser.add_argument("--width", dest="width", required=True)
    parser.add_argument(
        "--style",
        dest="style",
        required=True,
        choices=["bw", "color", "emoji", "line", "test", "four", "replace", "terminal"],
    )
    parser.add_argument(
        "--out", dest="out", required=True, choices=["html", "terminal", "video"]
    )

    args = parser.parse_args()

    input_file = args.input_file

    if is_video_file(args.input_file):
        video_to_frames(args.input_file)
        input_file = input_file.split("/")[-1].split(".")[0] + "_frame/"

    # if img_file is a file
    if os.path.isfile(input_file):
        convert_img(input_file, args.width, args.out, args.style)
    # if img_file is a directory
    else:
        files = os.listdir(input_file)
        files.sort()
        os.mkdir(input_file[:-1] + "_ascii/")
        for file in files:
            filename = input_file + file
            print(filename)
            convert_img(filename, args.width, args.out, args.style)


if __name__ == "__main__":
    parse_arg()
