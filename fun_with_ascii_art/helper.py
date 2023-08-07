"""Helper Functions
List of helper functions.

This file can also be imported as a module and contains the following
functions:

    * png_to_jpg : Converts PNG to JPG
    * check_input_type : Check if input file type is permitted
    * get_file_name : Get file name without the dir and extension info included
    * create_folder : Creates a folder if it doesn't exist
    * video_to_frames : Capture each frame of a video as an image and puts them in a folder
    * html_to_video : Converts html ascii files into a video
"""
import os
import glob
import cv2
from PIL import Image
from pytube import YouTube
import imgkit
from constants import IMG_EXTENSION, VIDEO_EXTENSION


def png_to_jpg(img_file: str):
    """Converts PNG to JPG

    Args:
        img_file (str): Path to an PNG image file

    Returns:
        str: Path to the JPG version of the image
    """
    img = Image.open(img_file).convert("RGB")
    new_file_name = img_file[:-4] + ".jpg"
    img.save(new_file_name, "jpeg")
    return new_file_name


def check_input_type(path: str):
    """Check if input file type is permitted

    Args:
        path (str): Path to an input file

    Returns:
        ["img", "video", "na", "folder"]: Type of the input file
    """
    if os.path.isfile(path):
        extension = path.split(".")[-1]
        if extension in IMG_EXTENSION:
            return "img"
        if extension in VIDEO_EXTENSION:
            return "video"
        raise TypeError('Check your file type')
    return "folder"


def get_file_name(path: str, prefix: str = "", postfix: str = ""):
    """Get file name without the dir and extension info included

    Args:
        path (str): Path to an input file
        prefix (str): Prefix for the name (default is "")
        postfix (str): Postfix for the name (default is "")

    Returns:
        str: Name of the file
    """
    return prefix + path.split("/")[-1].split(".")[0] + postfix


def create_folder(path: str):
    """Creates a folder if it doesn't exist

    Args:
        path (str): Path to create
    """
    if not os.path.exists(path):
        os.mkdir(path)


def video_to_frames(video_file: str):
    """Capture each frame of a video as an image and puts them in a folder

    Args:
        video_file (str): Path to a video file
    """
    vidcap = cv2.VideoCapture(video_file)
    success, image = vidcap.read()
    count = 0
    folder_path = get_file_name(video_file, "result/", "_frame/")
    create_folder(folder_path)

    while success:
        if count % 4 == 0:
            # save frame as JPEG file
            cv2.imwrite(f"{folder_path}{count}.jpg", image)
        success, image = vidcap.read()
        print("Read a new frame: ", success)
        count += 1


def html_to_video(folder: str):
    """Converts html ascii files into a video

    Args:
        folder (str): Path to a folder
    """
    img_array = []
    for filename in glob.glob(folder + "*.html"):
        img_file = filename.split(".")[0] + ".jpg"
        imgkit.from_file(filename, img_file)
        img = cv2.imread(img_file)
        img_array.append(img)

    size = (img_array[0].shape[0], img_array[0].shape[1])

    out = cv2.VideoWriter(
        "result/project.avi", cv2.VideoWriter_fourcc(*"DIVX"), 15, size
    )

    for img in img_array:
        out.write(img)

    out.release()


def extract_youtube_audio(url: str):
    """Extracts audio from a youtube video

    Args:
        url (str): Url of the video
    """
    selected_video = YouTube(url)

    audio = selected_video.streams.filter(only_audio=True, file_extension="mp4")[1]
    print(audio)

    audio.download()
