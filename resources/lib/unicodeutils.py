# coding=utf-8


def try_decode(text, encoding="utf-8"):
    if not isinstance(text, str):
        try:
            return text.decode(encoding)
        except:
            pass
    return text
