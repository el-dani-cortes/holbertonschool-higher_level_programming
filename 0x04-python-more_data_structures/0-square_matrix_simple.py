#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Function that prints a listfunction that
       computes the square value of all integers of a matrix.
    Args:
        matrix: 2 dimensional array.
    Returns:
        New matrix with square of the value of the original matrix.
    """
    new_matrix = []
    for item in matrix:
        list_square = list(map(lambda x: x ** 2, item))
        new_matrix.append(list_square)
    return new_matrix
