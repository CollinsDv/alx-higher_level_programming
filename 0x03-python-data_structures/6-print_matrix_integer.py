#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # handle an empty list
    if len(matrix) == 1:
        print("{}".format('$'))
    else:
        for row in matrix:
            for num in row:
                # handling elements in list except the last value
                if num != row[-1]:
                    print("{:d} ".format(num), end='')
                else:
                    print("{:d}$".format(num))
