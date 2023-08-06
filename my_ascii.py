"""Arg Parser
Parse given inputs and run the Ascii converter.

You can run this script by running a code like below
python3 my_ascii.py --file img/sohee.jpg --width 40 --style color --out html

This file can also be imported as a module and contains the following
functions:

    * convert_img : Convert PNG to JPG and creates/runs a converter
    * parse_arg : parses input args depending on the input file type
"""


import argparse
import os
from ImageObj import ImageObj
from AsciiConverter import AsciiConverter
from helper import (
    png_to_jpg,
    video_to_frames,
    check_input_type,
    get_file_name,
    create_folder,
    html_to_video,
)

Out = ["html", "terminal", "video"]
Style = ["bw", "color", "emoji", "line", "test", "four", "replace", "terminal"]


def convert_img(img_file: str, width: int, out: Out, style: Style, out_dir: str):
    """Creates and runs a AsciiConverter

    Args:
    img_file (str): Path to the image file
    width (int): Desired width of the output
    out (["html", "terminal", "video"]): Desired format of the output file
    style (["bw", "color", "emoji", "line", "test", "four", "replace", "terminal"]): Desired style of Ascii converting
    out_dir (str): Path to put the output file
    """
    if img_file.endswith(".png"):
        img_file = png_to_jpg(img_file)

    img = ImageObj(img_file, int(width))
    converter = AsciiConverter(img, out, style, out_dir)
    converter.convert()


def parse_arg():
    """Parses user input args"""
    # create an arg parser
    description = "Image to ASCII Art Converter"
    parser = argparse.ArgumentParser(description=description)

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
    input_type = check_input_type(args.input_file)

    if input_type == "na":
        print("Check your input file type")
        return
    if input_type == "img":
        convert_img(input_file, args.width, args.out, args.style, "result/")
    else:
        if input_type == "video":
            video_to_frames(input_file)
            input_file = get_file_name(input_file, "result/", "_frame/")
            destination = input_file[:-1] + "_ascii/"
        elif input_type == "folder":
            destination = "result/" + input_file[:-1] + "_ascii/"
        files = os.listdir(input_file)
        files.sort()
        create_folder(destination)
        for file in files:
            filename = input_file + file
            print("Converting " + filename + " to ascii.")
            convert_img(filename, args.width, args.out, args.style, destination)

        if input_type == "video":
            html_to_video(input_file[:-1] + "_ascii/")


if __name__ == "__main__":
    parse_arg()
