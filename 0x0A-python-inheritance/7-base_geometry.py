#!/usr/bin/python3
"""create class named BaseGeometry"""


class BaseGeometry:
    """class that calculates a area"""

    def area(self):
        """area method with a exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """some exceptions about value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
