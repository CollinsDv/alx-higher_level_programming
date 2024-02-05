#!/usr/bin/python3
"""import rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defines a square"""
    def __init__(self, size):
        self.integer_validator('size', size)

        self.__size = size
        super().__init__(size, size)
