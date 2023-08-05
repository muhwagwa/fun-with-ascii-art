import cv2
from PIL import Image
from constants import PERMITTED_EXTENSION


def png_to_jpg(img_file):
    img = Image.open(img_file).convert("RGB")
    new_file_name = img_file[:-4] + ".jpg"
    img.save(new_file_name, "jpeg")
    return new_file_name


def check_file_extension(file):
    extension = file.split(".")[-1]
    if extension in PERMITTED_EXTENSION:
        return True
    return False


def video_to_frames():
    vidcap = cv2.VideoCapture("video/bali.mov")
    success, image = vidcap.read()
    count = 0
    while success:
        if count % 4 == 0:
            # save frame as JPEG file
            cv2.imwrite("images/bali/frame%d.jpg" % count, image)
        success, image = vidcap.read()
        print("Read a new frame: ", success)
        count += 1
