import argparse
import glob
import os
import cv2
import imgkit
from ImageObj import ImageObj
from AsciiConverter import AsciiConverter
from helper import (
    png_to_jpg,
    video_to_frames,
    is_image_file,
    check_input_type,
    get_file_name,
    create_folder,
)


def convert_img(img_file, width, out, style, out_dir):
    if img_file.endswith(".png"):
        img_file = png_to_jpg(img_file)
    if not is_image_file(img_file):
        print(img_file + " is not an image file")
        return

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

    if input_type == "video":
        video_to_frames(args.input_file)
        input_file = get_file_name(input_file, "result/", "_frame/")

    # if input_file is a file
    if input_type == "img":
        convert_img(input_file, args.width, args.out, args.style, "result/")
    # if input_file is a directory
    elif input_type == "folder" or input_type == "video":
        files = os.listdir(input_file)
        files.sort()
        destination = input_file[:-1] + "_ascii/"
        create_folder(destination)
        for file in files:
            filename = input_file + file
            print(filename)
            convert_img(filename, args.width, args.out, args.style, destination)

    if input_type == "video":
        img_array = []
        dir = input_file[:-1] + "_ascii/"
        for filename in glob.glob(dir + "*.html"):
            img_file = filename.split(".")[0] + ".jpg"
            imgkit.from_file(filename, img_file)
            img = cv2.imread(img_file)
            height, width, layer = img.shape
            size = (width, height)
            img_array.append(img)

        out = cv2.VideoWriter(
            "result/project.avi", cv2.VideoWriter_fourcc(*"DIVX"), 15, size
        )

        for i in range(len(img_array)):
            out.write(img_array[i])

        out.release()


if __name__ == "__main__":
    parse_arg()
