#!/usr/bin/python3
"""class rectangle that have height and width as attributes"""


class Rectangle:
    """rectangle class have __init__ methode and getters and setters"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """private instance attribute and raise exceptions"""
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

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
            raise ValueError("width must be >= 0")
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
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """function that calculates the area of rectangle"""
        return self.height * self.width

    def perimeter(self):
        """function that calculates the perimeter of rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """function that prints a rectangle using #"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        new_rect = []
        for i in range(self.__height):
            for j in range(self.__width):
                new_rect.append(str(self.print_symbol))
            if i != self.__height - 1:
                new_rect.append('\n')
        new_rect = "".join(new_rect)
        return (new_rect)

    def __repr__(self):
        """create a representation of the rectangle"""
        rect = 'Rectangle('+str(self.width)+', '+str(self.height)+')'
        return rect

    def __del__(self):
        """when an instance is deleted, this message will be printed"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """check whick instance have the bigger area and returns it"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        if rect_1.area() >= rect_2.area():
            return rect_1
