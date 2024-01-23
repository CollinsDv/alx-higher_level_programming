#!/usr/bin/python3

"""Filename: 3-square.py"""


class Square:
	"""An class that defines a square with private attribute
	and returns the area
	Also handles use of setters and getters
	"""
	def __init__(self, size=0, position=(0, 0)):
		if type(size) is not int:
			raise TypeError("size must be an integer")
		else:
			if size < 0:
				raise ValueError("size must be >= 0")
			else:
				self.__size = size

	@property
	def size(self):
		return self.__size

	@property
	def position(self):
		return self.__position

	@size.setter
	def size(self, value):
		if type(value) is not int:
			raise TypeError("size must be an integer")
		else:
			if value < 0:
				raise ValueError("size must be >= 0")
			else:
				self.__size = value

	@position.setter
	def position(self, value):
		if type(value) is not tuple or len(value) != 2 or type(value[0]) is not int
		and type(value[1]) is not int or value[0] < 0 or value[1] < 0:
			raise TypeError("position must be a tuple of 2 positive
							 integers")
		else:
			self.__position = value

	def area(self):
		return self.__size * self.__size

	def my_print(self):
		def my_print(self):
			"""Print method"""
		if (self.size == 0):
			print()
		else:
			for i in range(self.position[1]):
				print()
			for j in range(0, self.size):
				for e in range(self.position[0]):
					print(" ", end="")
				for j in range(self.size):
					print("#", end="")
				print() 
