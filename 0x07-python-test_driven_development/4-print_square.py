#!/usr/bin/python3

"""
module: 4-print_square.py
Args:
    size (int)
"""


def print_square(size):
    """print a square with '#'."""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            for j in range(size):
                print('#', end='')
            print()
