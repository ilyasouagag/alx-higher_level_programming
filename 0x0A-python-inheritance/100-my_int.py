#!/usr/bin/python3
"""class that inherits from int"""


class MyInt(int):
    """function that invert == and !="""

    def __eq__(self, value):
        """invert == to !="""
        return self.real != value

    def __ne__(self, value):
        """invert != to =="""
        return self.real == value
