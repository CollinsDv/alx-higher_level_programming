#!/usr/bin/python3
"""Rectangle inheritance"""
from models.base import Base


class Rectangle(Base):
    """defining a rectangle class
    inherited from Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""

        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """heigth getter""" 
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return area of a rectagle"""
        return self.__width * self.__height

    def display(self):
        """print the rectangle instance with '#'
        """
        for hght in range(self.y):
            print()
        for x in range(self.height):
            for wdth in range(self.x):
                print(' ', end='')
            for y in range(self.width):
                print('#', end='' if y < self.width - 1 else '\n')

    def update(self, *args, **kwargs):
        '''
        Allows for variadic args
        '''
        if args and len(args) > 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except:
                pass
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'y' in kwargs:
                self.y = kwargs['y']
            if 'x' in kwargs:
                self.x = kwargs['x']

    def to_dictionary(self):
        """return dict representation of a Rectangle"""
        return {'x' : self.x, 'y' : self.y , 'id' : self.id, 'height' : self.height,
                'width' : self.width}
  
    def __str__(self):
        """return string object representation"""
        return "[{}] ({}) {}/{} - {}/{}".format(
                type(self).__name__, self.id, self.x, self.y,
                self.width, self.height)
