"""Exceptions
Parse given inputs and run the Ascii converter.

You can run this script by running a code like below
python3 my_ascii.py --file img/sohee.jpg --width 40 --style color --out html

This file can also be imported as a module and contains the following
functions:

    * raise_file_doesnt_exist : Raised when a path doesn't exist
    * raise_invalid_file_type : Raised when a file has unsupported file type
"""
import sys


def raise_file_doesnt_exist(path: str):
    """Raised when a path doesn't exist

    Args:
    path (str): Path to the file that doesn't exist
    """
    sys.exit(f"File/Folder '{path}' does not exist")


def raise_invalid_file_type(path: str):
    """Raised when a file has unsupported file type

    Args:
    path (str): Path to the file that has invalid file type
    """
    sys.exit(f"File type is not supported. Check your file '{path}'.")
