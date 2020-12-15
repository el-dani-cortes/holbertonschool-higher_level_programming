#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Function that prints a matrix of integers

    Args:
        matrix: matrix of integers to print

    Returns:
        Return always nothing
    """
    for row in matrix:
        for item in row:
            if item != row[-1]:
                print("{:d}".format(item), end=' ')
            else:
                print(item, end='')
        print("")
