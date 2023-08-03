import argparse
import os
from PIL import Image
from ImageObj import ImageObj
from AsciiConverter import AsciiConverter


def png_to_jpg(img_file):
    img = Image.open(img_file).convert("RGB")
    new_file_name = img_file[:-4] + ".jpg"
    img.save(new_file_name, "jpeg")
    return new_file_name


if __name__ == "__main__":
    # create arg parser
    DESCRIPTION = "Image to ASCII Art Converter"
    parser = argparse.ArgumentParser(description=DESCRIPTION)

    parser.add_argument("--file", dest="imgFile", required=True)
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

    def convert_img(img_file):
        # check file extension
        if img_file.endswith(".png"):
            img_file = png_to_jpg(img_file)
        elif not img_file.endswith(".jpg") and not img_file.endswith(".jpeg"):
            print(img_file + " is not an image file")
            return

        img = ImageObj(img_file, int(args.width))
        converter = AsciiConverter(img, args.out, args.style)
        converter.convert()

    # file
    if os.path.isfile(args.imgFile):
        convert_img(args.imgFile)
    # directory
    else:
        files = os.listdir(args.imgFile)
        files.sort()
        for file in files:
            filename = args.imgFile + "/" + file
            print(filename)
            convert_img(filename)
