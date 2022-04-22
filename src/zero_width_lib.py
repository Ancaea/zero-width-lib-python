_ZERO_WIDTH_NON_JOINER = '‌'
_ZERO_WIDTH_JOINER = '‍'
_ZERO_WIDTH_SPACE = '​'
_ZERO_WIDTH_NO_BREAK_SPACE = '﻿'
_LEFT_TO_RIGHT_MARK = '‎'
_RIGHT_TO_LEFT_MARK = '‏'

zeroWidthDict = {
    _LEFT_TO_RIGHT_MARK: _LEFT_TO_RIGHT_MARK,
    _RIGHT_TO_LEFT_MARK: _RIGHT_TO_LEFT_MARK,
    _ZERO_WIDTH_NON_JOINER: _ZERO_WIDTH_NON_JOINER,
    _ZERO_WIDTH_JOINER: _ZERO_WIDTH_JOINER,
    _ZERO_WIDTH_NO_BREAK_SPACE: _ZERO_WIDTH_NO_BREAK_SPACE,
    _ZERO_WIDTH_SPACE: _ZERO_WIDTH_SPACE
}

_Quinary2ZeroMap: list = list(zeroWidthDict.values())
_Zero2QuinaryMap: dict = {index: values for values, index in enumerate(_Quinary2ZeroMap)}


def _is_visible(char: str) -> bool:
    return char not in _Zero2QuinaryMap


def _find_first_visible(text: str):
    for index, char in enumerate(text):
        if _is_visible(char):
            return index
    return -1


def _to_any_base(number: int, radix: int) -> str:
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
        base5 = _to_any_base(int(base10), 5)
        zero = ''.join([_Quinary2ZeroMap[int(each)] for each in list(base5)])
        z = z + zero + _ZERO_WIDTH_SPACE
    return z[:-1]


def z2t(z: str) -> str:
    t = ''
    if len(z) == 0:
        return t

    char: str
    for char in z.split(_ZERO_WIDTH_SPACE):
        base5 = ''.join([str(_Zero2QuinaryMap[each]) for each in list(char)])
        t += chr(int(base5, 5))
    return t


def encode(visible: str, hidden: str) -> str:
    hid2z = t2z(hidden)
    if len(visible) == 0:
        return hid2z

    e = f"{visible[:1]}{hid2z}{visible[1:]}"
    return e


def extract(text: str) -> dict[str]:
    first_visible = _find_first_visible(text)
    second_visible = _find_first_visible(text[first_visible + 1:])
    visible = ''
    hidden = ''

    for char in text[:second_visible + 1]:
        if _is_visible(char):
            visible += char
        else:
            hidden += char

    for char in text[second_visible - 1:]:
        if _is_visible(char):
            visible += char

    return {"visible": visible,
            "hidden": hidden}


def decode(visible: str) -> str:
    return z2t(extract(visible)['hidden'])


def split(text: str) -> str:
    second_visible = _find_first_visible(text[1:])
    result = text[:second_visible + 1]
    split_list = text[second_visible + 1:]
    for char in split_list:
        result += f"{char}{_ZERO_WIDTH_SPACE}"
    return result
