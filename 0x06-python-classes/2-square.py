#!/usr/bin/python3

"""Filename: 2-square.py"""


class Square:
    """An class that defines a square without private attribute:"""
    def __init__(self, size=0):
        try:
            size = int(size)
        except TypeError:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
