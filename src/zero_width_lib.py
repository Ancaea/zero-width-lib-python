ZERO_WIDTH_NON_JOINER = '‌'
ZERO_WIDTH_JOINER = '‍'
ZERO_WIDTH_SPACE = '​'
ZERO_WIDTH_NO_BREAK_SPACE = '﻿'
LEFT_TO_RIGHT_MARK = '‎'
RIGHT_TO_LEFT_MARK = '‏'

zeroWidthDict = {
    LEFT_TO_RIGHT_MARK: LEFT_TO_RIGHT_MARK,
    RIGHT_TO_LEFT_MARK: RIGHT_TO_LEFT_MARK,
    ZERO_WIDTH_NON_JOINER: ZERO_WIDTH_NON_JOINER,
    ZERO_WIDTH_JOINER: ZERO_WIDTH_JOINER,
    ZERO_WIDTH_NO_BREAK_SPACE: ZERO_WIDTH_NO_BREAK_SPACE,
    ZERO_WIDTH_SPACE: ZERO_WIDTH_SPACE
}

Quinary2ZeroMap: list = list(zeroWidthDict.values())
Zero2QuinaryMap: dict = {index: values for values, index in enumerate(Quinary2ZeroMap)}


def is_visible(char: str) -> bool:
    return char not in Zero2QuinaryMap


def find_first_visible(text: str):
    for index, char in enumerate(text):
        if is_visible(char):
            return index
    return -1


def to_any_base(number: int, radix: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-={}[]|\\:\";\'<>?,./`~"
    max_radix = len(digits)
    if 2 > radix > max_radix:
        raise ValueError(f"Limit exceeded.")

    remstack = []

    while number > 0:
        rem = number % radix
        remstack.append(rem)
        number = number // radix

    result = ""
    while len(remstack):
        result += digits[remstack.pop()]

    return result


def t2z(t: str) -> str:
    z = ''
    char: str
    for char in list(t):
        base10 = ord(char)
        base5 = to_any_base(int(base10), 5)
        zero = ''.join([Quinary2ZeroMap[int(each)] for each in list(base5)])
        z = z + zero + ZERO_WIDTH_SPACE
    return z[:-1]


def z2t(z: str) -> str:
    t = ''
    if len(z) == 0:
        return t

    char: str
    for char in z.split(ZERO_WIDTH_SPACE):
        base5 = ''.join([str(Zero2QuinaryMap[each]) for each in list(char)])
        t += chr(int(base5, 5))
    return t


def encode(visible: str, hidden: str) -> str:
    hid2z = t2z(hidden)
    if len(visible) == 0:
        return hid2z

    e = f"{visible[:1]}{hid2z}{visible[1:]}"
    return e


def extract(text: str) -> dict[str]:
    first_visible = find_first_visible(text)
    second_visible = find_first_visible(text[first_visible + 1:])
    visible = ''
    hidden = ''

    for char in text[:second_visible + 1]:
        if is_visible(char):
            visible += char
        else:
            hidden += char

    for char in text[second_visible - 1:]:
        if is_visible(char):
            visible += char

    return {"visible": visible,
            "hidden": hidden}


def decode(visible: str) -> str:
    return z2t(extract(visible)['hidden'])


def split(text: str) -> str:
    second_visible = find_first_visible(text[1:])
    result = text[:second_visible + 1]
    split_list = text[second_visible + 1:]
    for char in split_list:
        result += f"{char}{ZERO_WIDTH_SPACE}"
    return result
