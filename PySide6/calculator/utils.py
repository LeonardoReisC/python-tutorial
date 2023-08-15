import re

NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')


def isNumOrDot(string: str):
    return bool(NUM_OR_DOT_REGEX.search(string))


def isEmpty(string: str):
    return string == ''


def isValidNumber(string: str):
    isValid = False

    try:
        float(string)
        isValid = True
    finally:
        return isValid


def converToNumber(string: str):
    number = float(string)

    if number.is_integer():
        number = int(number)

    return number
