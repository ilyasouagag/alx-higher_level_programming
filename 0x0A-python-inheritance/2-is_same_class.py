#!/usr/bin/python3
"""function that returns True if object is exactly an instance"""


def is_same_class(obj, a_class):
    """check if an objec is an instance"""
    return type(obj) is a_class
