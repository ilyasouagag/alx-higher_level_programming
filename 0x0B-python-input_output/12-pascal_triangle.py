#!/usr/bin/python3
"""eturns a list of lists of integers
representing the Pascal’s triangle"""


def pascal_triangle(n):
    """eturns a list of lists of integers
    representing the Pascal’s triangle"""
    if n <= 0:
        return []
    array = [[1]]
    while len(array) != n:
        triangle = array[-1]
        temp = [1]
        for i in range(len(triangle) - 1):
            temp.append(triangle[i] + triangle[i+1])
        temp.append(1)
        array.append(temp)
    return array
