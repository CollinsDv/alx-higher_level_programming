#!/usr/bin/python3
"""file: 8-base_geometry.py
"""


class BaseGeometry():
    """handles inheritance"""
    def area(self):
        """raise an error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate parameter values

            Args:
                name (str): string parameter
                value (int): integer parameter
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """handle checksum of values without
    getters and setters
    """
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('height', height)

        self.__width = width
        self.__height = height
        
        
