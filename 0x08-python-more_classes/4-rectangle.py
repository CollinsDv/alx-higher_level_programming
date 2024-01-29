#!/usr/bin/python3

"""defining an rectangle"""


class Rectangle:
    """A class with Pythonic getters and setters"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        string = ''

        if self.__height == 0 or self.__width == 0:
            return string

        for i in range(self.__height):
            for j in range(self.__width):
                string += '#'
            if i != self.__height - 1:
                string += '\n'

        return string

    def __repr__(self):
        return ("Rectangle(" + str(self.__width)
                + ", " + str(self.__height) + ")")
