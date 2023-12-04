#!/usr/bin/python3
"""lass Rectangle inherits from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""create class named Rectangle"""


class Rectangle(BaseGeometry):
    """class that inherits from basegeometry"""

    def __init__(self, width, height):
        """initialise atributtes for instances"""
        self.__width = width
        self.__height = height
        super().integer_validator('width', self.__width)
        super().integer_validator('height', self.__height)

    def area(self):
        """calculate the area of rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """print a description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
