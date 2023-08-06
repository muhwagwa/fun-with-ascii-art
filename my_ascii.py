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


def convert_img(img_file, width, out, style, out_dir):
    if img_file.endswith(".png"):
        img_file = png_to_jpg(img_file)

    img = ImageObj(img_file, int(width))
    converter = AsciiConverter(img, out, style, out_dir)
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
    input_type = check_input_type(args.input_file)

    if input_type == "na":
        print("Check your input file type")
        return
    elif input_type == "img":
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
