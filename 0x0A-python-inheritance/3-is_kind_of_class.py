#!/usr/bin/python3
"""function that returns True if the object is an instance of, or if the object is
an instance of a class that inherited from"""


def is_kind_of_class(obj, a_class):
    """return true if it is else False"""
    return isinstance(obj, a_class)
