import cv2
from PIL import Image
from constants import IMG_EXTENSION, VIDEO_EXTENSION
import os


def png_to_jpg(img_file):
    img = Image.open(img_file).convert("RGB")
    new_file_name = img_file[:-4] + ".jpg"
    img.save(new_file_name, "jpeg")
    return new_file_name


def check_input_type(path):
    if os.path.isfile(path):
        extension = path.split(".")[-1]
        if extension in IMG_EXTENSION:
            return "img"
        elif extension in VIDEO_EXTENSION:
            return "video"
        return "na"
    return "folder"


def is_image_file(file):
    extension = file.split(".")[-1]
    if extension in IMG_EXTENSION:
        return True
    return False


def get_file_name(path, prefix="", postfix=""):
    return prefix + path.split("/")[-1].split(".")[0] + postfix


def create_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)


def video_to_frames(video_file):
    vidcap = cv2.VideoCapture(video_file)
    success, image = vidcap.read()
    count = 0
    folder_path = get_file_name(video_file, "result/", "_frame/")
    create_folder(folder_path)

    while success:
        if count % 4 == 0:
            # save frame as JPEG file
            cv2.imwrite(folder_path + "%d.jpg" % count, image)
        success, image = vidcap.read()
        print("Read a new frame: ", success)
        count += 1
