#!/usr/bin/python3
"""Rectangle Module"""

from .base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """function that initialize instance attributes"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area of  the rectangle"""
        return self.__height * self.__width

    def display(self):
        """prints in stdout the rectangle with #"""
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for k in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """return a representation"""
        return f"[Rectangle] ({self.id}) {self.x}/\
{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """update values by the ones given as parameters"""
        if args and len(args) != 0:
            self.__init__(self.width, self.height, self.x, self.y)
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs and len(kwargs) != 0:
            for a in kwargs:
                if a == "id":
                    self.id = kwargs[a]
                elif a == "width":
                    self.width = kwargs[a]
                elif a == "height":
                    self.height = kwargs[a]
                elif a == "x":
                    self.x = kwargs[a]
                elif a == "y":
                    self.y = kwargs[a]

    def to_dictionary(self):
        """create dictionnary"""
        return {'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width}
