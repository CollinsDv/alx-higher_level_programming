#!/usr/bin/python3
"""file: 6-base_geometry.py
"""


class BaseGeometry():
    """handle undefined method"""
    def area(self):
        """raise an error"""
        raise Exception("area() is not implemented")
