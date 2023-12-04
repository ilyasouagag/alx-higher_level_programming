#!/usr/bin/python3
"""class Rectangle inherits from BaseGeometry."""

Rectangle = __import__('9-rectangle').Rectangle

"""create class named Square"""


class Square(Rectangle):
    """representation of a square"""

    def __init__(self, size):
        """initialize attributes for instance"""
        self.__size = size
        super().integer_validator('size', self.__size)
        super().__init__(size, size)
