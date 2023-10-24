#!/usr/bin/python3
"""this is the fourth task of the project"""


class Square:
    """class that defines a square"""

    def __init__(self, size=0):
        """private instance attribute and raise exceptions"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the current square of area"""
        return self.__size * self.__size
