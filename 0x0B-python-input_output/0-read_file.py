#!/usr/bin/python3
"""file: 0-read_file
"""


def read_file(filename=""):
    """read lines of a file

    Args:
        filename (str): name of the file

    Result:
        printed lines

    """
    if type(filename) is not str:
        raise ValueError("filename has to be a string")

    with open(filename, encoding="UTF-8") as file:
        for line in file:
            print(line, end='')
