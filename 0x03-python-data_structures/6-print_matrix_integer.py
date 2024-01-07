#!/usr/bin/python3
'''
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if len(row) == 0:
            print('$')
        for n in range(len(row)):
            print('{:d}'.format(row[n]),
                  end='\n' if n == len(row) - 1 else ' ')
'''
def print_matrix_integer(matrix=[[]]):
    # handle an empty list
    if not matrix or any(not row for row in matrix):
        print()
    else:
        for row in matrix:
            for num in row:
                # handling elements in list except the last value
                if num != row[-1]:
                    print("{:d} ".format(num), end='')
                else:
                    print("{:d}".format(num))
