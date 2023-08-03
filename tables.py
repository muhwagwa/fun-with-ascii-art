def default(check):
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


def test(check):
    if check == [1, 1, 1, 1]:
        return "&nbsp;"
    return "8"


def korean(check):
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


def line(check):
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


def line2(check):
    if check == [1, 1, 1, 1]:
        return "&nbsp;"
    return "-"


def emoji(check):
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
