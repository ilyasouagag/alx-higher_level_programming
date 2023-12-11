#!/usr/bin/python3
"""class Square"""
from .rectangle import Rectangle

class Square(Rectangle):
    """iherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """return a representation"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """update the class"""
        if args and len(args) != 0:
            self.__init__(self.size, self.x, self.y)
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs and len(kwargs) != 0:
            for a, b in kwargs.items():
                if a == "id":
                    self.id = b
                elif a == "size":
                    self.size = b
                elif a == "x":
                    self.x = b
                elif a == "y":
                    self.y = b

    def to_dictionary(self):
        """create dictionnary"""
        return {'id': self.id, 'x': self.x, 'size': self.height, 'y': self.y}
