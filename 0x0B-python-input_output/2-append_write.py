#!/usr/bin/python3
"""establish append operation
"""


def append_write(filename="", text=""):
    """open a file and append content

    Args:
        filename (str) - the filename
        text (str) - text to append
    """
    with open(filename, mode='a', encoding='UTF-8') as file:
        return file.write(text)
