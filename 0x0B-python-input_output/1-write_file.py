#!/usr/bin/python3
"""establish write operation
"""


def write_file(filename="", text=""):
    """open a file and overwrite it
    """
    with open(filename, mode='w', encoding='UTF-8') as file:
        return file.write(text)
