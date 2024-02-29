#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in unsorted integers"""

    if list_of_integers is None or list_of_integers == []:
        return None
    base = 0
    length = len(list_of_integers)
    center = ((length - base) // 2) + base
    center = int(center)
    if length == 1:
        return list_of_integers[0]
    if length == 2:
        return max(list_of_integers)
    if list_of_integers[center] >= list_of_integers[center - 1] and\
            list_of_integers[center] >= list_of_integers[center + 1]:
        return list_of_integers[center]
    if center > 0 and list_of_integers[center] < list_of_integers[center + 1]:
        return find_peak(list_of_integers[center:])
    if center > 0 and list_of_integers[center] < list_of_integers[center - 1]:
        return find_peak(list_of_integers[:center])
