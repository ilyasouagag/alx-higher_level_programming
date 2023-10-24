#!/usr/bin/python3
"""this is the seventh task of the project"""


class Square:
    """class that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """private instance attribute and raise exceptions"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """get the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """set the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """get the position"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                any(num < 0 for num in value) or
                any(not isinstance(num, int) for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns the current square of area"""
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with #"""
        if self.__size == 0:
            print()
            return
        for k in range(0, self.__position[1]):
            print()
        for i in range(self.__size):
            for n in range(0, self.__position[0]):
                print(' ', end='')
            for j in range(self.__size):
                print('#', end='')
            print()
