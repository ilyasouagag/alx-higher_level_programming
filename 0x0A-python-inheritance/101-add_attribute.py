#!/usr/bin/python3
"""function that adds a new attribute to a class"""


def add_attribute(obj, attr, value):
    """dict attribute is a dictionnary that stores
    the object's attributes"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add a new attribute")
    setattr(obj, attr, value)
