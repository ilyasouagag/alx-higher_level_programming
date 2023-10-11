#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return []
    return list(map(lambda row: list(map(lambda x: x**2, row)), matrix))

