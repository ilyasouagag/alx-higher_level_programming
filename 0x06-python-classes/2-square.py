#!/usr/bin/python3
"""this is the third task of the project"""


class Square:
    """class that defines a square"""

    def __init__(self, size=0):
        """private instance attribute and raise exceptions"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
