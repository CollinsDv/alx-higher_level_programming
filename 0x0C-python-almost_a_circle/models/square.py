#!/usr/bin/python3
"""Square definition"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defining a sqaure class
    inherited from Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''
        Allows for variadic number of arguements
        '''
        if args and len(args) > 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except Exception:
                pass
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.width = kwargs['size']
            if 'y' in kwargs:
                self.y = kwargs['y']
            if 'x' in kwargs:
                self.x = kwargs['x']

    def to_dictionary(self):
        """return dict representation of a square"""
        return {'id': self.id, 'x': self.x,
                'size': self.size, 'y': self.y}

    def __str__(self):
        return "[{}] ({}) {}/{} - {}".format(
                type(self).__name__, self.id, self.x, self.y,
                self.width)
