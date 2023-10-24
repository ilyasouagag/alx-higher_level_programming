#!/usr/bin/python3
import math

"""magicclass calculate the area and circumferenece of a circle"""


class MagicClass:
    """representation of circle"""

    def __init__(self, radius):
        """all attributes of object of MagicClass"""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self._MagicClass__radius = radius

    def area(self):
        """return the area of MagicClass"""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """return the circumference of the magicClass"""
        return 2 * math.pi * self._MagicClass__radius
