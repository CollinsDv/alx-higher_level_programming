#!/usr/bin/python3

"""
0-add_integer: implements a add function
add_integer: adds two integers
Return: sum in int format
"""


def add_integer(a, b=98):
    """
    Return sum of two integers.
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
