#!.usr/bin/python3
"""
file: 1-matrix_divided
args: matrix (list obj)
      div (int)
"""


def matrix_divided(matrix, div):
    """divide matrix by div"""
    new_list = []
    if type(matrix) is not list or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    length = len(matrix[0])

    for alist in matrix:
        if type(alist) is not list or not all(isinstance(num, (int, float))
                                              for num in alist):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        if len(alist) != length:
            raise TypeError("Each row of the matrix must have the same size")
        sub_list = [round(num / div, 2) for num in alist]
        new_list.append(sub_list)

    return new_list
