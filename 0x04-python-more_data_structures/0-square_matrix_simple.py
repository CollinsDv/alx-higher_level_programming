#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mult = lambda x : x * x

    return [[mult(num) for num in row] for row in matrix]
