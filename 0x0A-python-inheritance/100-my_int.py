#!/usr/bin/python3
'''
Write a class MyInt that inherits from int
'''


class MyInt(int):
	"""assign __eq__ to __ne__ and vice versa"""
    def __eq__(self, value):
        return int(self) != int(value)

    def __ne__(self, value):
        return int(self) == int(value)
