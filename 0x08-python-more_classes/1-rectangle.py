#!/usr/bin/python3
"""class rectangle that have height and width as attributes"""


class Rectangle:
    """rectangle class have __init__ methode and getters and setters"""

    def __init__(self, width=0, height=0):
        """private instance attribute and raise exceptions"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """return the current width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set a new value to width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return the current height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set a new value to height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
