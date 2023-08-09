"""Arg Parser
Parse given inputs and run the Ascii converter.

You can run this script by running a code like below
python3 my_ascii.py --file img/sohee.jpg --width 40 --style color --out html

This file can also be imported as a module and contains the following
functions:

    * convert_img : Converts an image file to ascii
    * convert_video : Converts a video file to ascii
    * convert_folder : Converts all files in a folder to ascii
    * parse_arg : parses input args depending on the input file type
"""
import argparse
import os
from image_obj import ImageObj
from ascii_converter import AsciiConverter
from helper import (
    png_to_jpg,
    video_to_frames,
    check_input_type,
    get_file_name,
    create_folder,
    html_to_video,
)

STYLE = ["default", "emoji", "line", "underscore", "terminal", "korean"]
COLOR = ["bw", "grayscale", "color"]


def convert_img(
    img_file: str, width: int, style: STYLE, color: COLOR, destination: str
):
    """Converts an image file to ascii

    Args:
    img_file (str): Path to an image file
    width (int): Desired width of the output
    style (Style): Desired style of Ascii converting
    color (COLOR): Desired color of the result
    destination (str): Path to put the output file
    """
    if img_file.endswith(".png"):
        img_file = png_to_jpg(img_file)

    img = ImageObj(img_file, int(width))
    converter = AsciiConverter(img, style, color, destination)
    converter.convert()


def convert_video(video_file: str, width: int, style: STYLE, color: COLOR):
    """Converts a video file to ascii

    Args:
    video_file (str): Path to a video file
    width (int): Desired width of the output
    style (Style): Desired style of Ascii converting
    color (COLOR): Desired color of the result
    """
    video_to_frames(video_file)
    frame_folder = get_file_name(video_file, "result/", "_frame/")
    frame_ascii_folder = frame_folder[:-1] + "_ascii/"
    convert_folder(frame_folder, width, style, color, frame_ascii_folder)
    html_to_video(frame_ascii_folder)


def convert_folder(
    input_folder: str, width: int, style: STYLE, color: COLOR, destination: str = ""
):
    """Converts all files in a folder to ascii

    Args:
    input_folder (str): Path to a folder
    width (int): Desired width of the output
    style (Style): Desired style of Ascii converting
    color (COLOR): Desired color of the result
    destination (str): Path to put the output file
    """
    destination = (
        "result/" + input_folder[:-1] + "_ascii/" if destination == "" else destination
    )
    files = [file for file in os.listdir(input_folder) if not file.startswith(".")]
    files.sort()
    if style != "terminal":
        create_folder(destination)
    for file in files:
        filename = input_folder + file
        print("Converting " + filename + " to ascii.")
        file_type = check_input_type(filename)
        if file_type == "img":
            convert_img(filename, width, style, color, destination)
        elif file_type == "video":
            convert_video(filename, width, style, color)
        elif file_type == "folder":
            convert_folder(filename, width, style, color)


def parse_arg():
    """Parses user input args"""
    # create an arg parser
    description = "Image to ASCII Art Converter"
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument("--file", dest="input_file", required=True)
    parser.add_argument("--width", dest="width", required=True, type=int)
    parser.add_argument(
        "--style",
        dest="style",
        required=True,
        choices=STYLE,
    )
    parser.add_argument(
        "--color",
        dest="color",
        default="grayscale",
        choices=COLOR,
    )

    args = parser.parse_args()

    input_file = args.input_file
    input_type = check_input_type(args.input_file)
    input_color = "emoji" if args.style == "emoji" else args.color

    if input_type == "img":
        convert_img(input_file, args.width, args.style, input_color, "result/")
    elif input_type == "video":
        convert_video(input_file, args.width, args.style, input_color)
    elif input_type == "folder":
        convert_folder(input_file, args.width, args.style, input_color)


if __name__ == "__main__":
    parse_arg()
