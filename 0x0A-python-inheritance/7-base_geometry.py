#!/usr/bin/python3
"""file: 7-base_geometry.py
"""


class BaseGeometry():
    """handle undefined method"""
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
