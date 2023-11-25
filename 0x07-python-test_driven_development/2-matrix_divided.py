#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(matrix,list) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row,list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for num in row:
            if not isinstance(num,(int,float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")        
    if matrix:
        a = len(matrix[0])
    for i in range(1,len(matrix)):
        if len(matrix[i]) != a:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div,(int,float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise  ZeroDivisionError("division by zero")
    new_matrix = list(map(lambda row: 
                        list(map(lambda x: round((x/div),2),row)),matrix))
    return new_matrix
