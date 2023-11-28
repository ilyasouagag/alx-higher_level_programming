#!/usr/bin/python3
"""class named Locked class"""


class LockedClass:
    """class who will refuse to create any instance not named 'first_name'"""
    __slots__ = ('first_name',)
