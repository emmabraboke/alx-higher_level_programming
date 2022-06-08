#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    for i in matrix:
        values = []
        for j in i:
            values.append(j**2)
        new_matrix.append(values)
    return new_matrix
