#!/usr/bin/python3
"""function that returns True if the object
is an instance of a class that
inherited (directly or indirectly) from the specified class """


def inherits_from(obj, a_class):
    """true if the object is instance of a class"""
    if issubclass(type(obj),a_class):
        return True
    return False
