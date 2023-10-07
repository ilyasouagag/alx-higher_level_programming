#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for row in matrix:
        for item in row:
            print("{:d}".format(item), end="\n" if item == row[-1] else " ")
