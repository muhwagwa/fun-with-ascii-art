"""Converting Tables
Tables for converting array to an ASCII letter

This file can also be imported as a module and contains the following
functions:

    * default : default table
    * korean : table with korean characters
    * line : line table with horizontal, vertical and diagonal lines
    * underscore : line table with '_' only
    * emoji : apple emoji table
"""


def default(check: list):
    """Default table

    Args:
        check (list): Info of a 2x2 tile

    Returns:
        str: ASCII letter
    """
    result = ""
    match check:
        case [0, 0, 0, 1]:
            result = "."
        case [0, 0, 1, 0]:
            result = "."
        case [0, 1, 0, 0]:
            result = "'"
        case [1, 0, 0, 0]:
            result = "'"
        case [0, 0, 1, 1]:
            result = "_"
        case [0, 1, 0, 1]:
            result = "|"
        case [1, 0, 0, 1]:
            result = "\\"
        case [0, 1, 1, 0]:
            result = "/"
        case [1, 0, 1, 0]:
            result = "|"
        case [1, 1, 0, 0]:
            result = "-"
        case [0, 1, 1, 1]:
            result = "d"
        case [1, 1, 0, 1]:
            result = "q"
        case [1, 0, 1, 1]:
            result = "b"
        case [1, 1, 1, 0]:
            result = "P"
        case [1, 1, 1, 1]:
            result = "@"
    return result


def korean(check: list):
    """Table with korean characters

    Args:
        check (list): Info of a 2x2 tile

    Returns:
        str: ASCII letter
    """
    result = ""
    match check:
        case [0, 0, 0, 1]:
            result = "."
        case [0, 0, 1, 0]:
            result = "."
        case [0, 1, 0, 0]:
            result = "'"
        case [1, 0, 0, 0]:
            result = "'"
        case [0, 0, 1, 1]:
            result = "ㅡ"
        case [0, 1, 0, 1]:
            result = "ㅣ"
        case [1, 0, 0, 1]:
            result = "\\"
        case [0, 1, 1, 0]:
            result = "/"
        case [1, 0, 1, 0]:
            result = "ㅣ"
        case [1, 1, 0, 0]:
            result = "ㅈ"
        case [0, 1, 1, 1]:
            result = "ㅍ"
        case [1, 1, 0, 1]:
            result = "ㄱ"
        case [1, 0, 1, 1]:
            result = "ㄴ"
        case [1, 1, 1, 0]:
            result = "ㅌ"
        case [1, 1, 1, 1]:
            result = "ㅁ"
    return result


def line(check: list):
    """Line table with horizontal, vertical and diagonal lines

    Args:
        check (list): Info of a 2x2 tile

    Returns:
        str: ASCII letter
    """
    result = ""
    match check:
        case [0, 0, 0, 1]:
            result = "/"
        case [0, 0, 1, 0]:
            result = "\\"
        case [0, 1, 0, 0]:
            result = "\\"
        case [1, 0, 0, 0]:
            result = "/"
        case [0, 0, 1, 1]:
            result = "_"
        case [0, 1, 0, 1]:
            result = "|"
        case [1, 0, 0, 1]:
            result = "\\"
        case [0, 1, 1, 0]:
            result = "/"
        case [1, 0, 1, 0]:
            result = "|"
        case [1, 1, 0, 0]:
            result = "-"
        case [0, 1, 1, 1]:
            result = "/"
        case [1, 1, 0, 1]:
            result = "\\"
        case [1, 0, 1, 1]:
            result = "\\"
        case [1, 1, 1, 0]:
            result = "/"
        case [1, 1, 1, 1]:
            result = "&nbsp;"
    return result


def underscore(check: list):
    """Line table with '_' only

    Args:
        check (list): Info of a 2x2 tile

    Returns:
        str: ASCII letter
    """
    if check == [1, 1, 1, 1]:
        return "&nbsp;"
    return "-"


def emoji(check: list):
    """Apple emoji table

    Args:
        check (list): Info of a 2x2 tile

    Returns:
        str: ASCII letter
    """
    result = ""
    match check:
        case [0, 0, 0, 1]:
            result = "128167"
        case [0, 0, 1, 0]:
            result = "128161"
        case [0, 1, 0, 0]:
            result = "128205"
        case [1, 0, 0, 0]:
            result = "127853"
        case [0, 0, 1, 1]:
            result = "128371"
        case [0, 1, 0, 1]:
            result = "128738"
        case [1, 0, 0, 1]:
            result = "127746"
        case [0, 1, 1, 0]:
            result = "127752"
        case [1, 0, 1, 0]:
            result = "128067"
        case [1, 1, 0, 0]:
            result = "127796"
        case [0, 1, 1, 1]:
            result = "127953"
        case [1, 1, 0, 1]:
            result = "128299"
        case [1, 0, 1, 1]:
            result = "128208"
        case [1, 1, 1, 0]:
            result = "127940"
        case [1, 1, 1, 1]:
            result = "127749"
    return result
