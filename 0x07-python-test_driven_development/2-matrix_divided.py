#!/usr/bin/python3
"""Module that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix
       by another number.

    Args:
       matrix(list): List with items of ints or floats to divide(dividends).
       div(int or float): Number to use as divisor in the division.

    Returns:
       A list with the result of every division.

    Raises:
        TypeError: if matrix and its elements are
                   not integer or float data types.
        TypeError: If rows of the matrix have diferent size.
        TypeError: If div variale is not an int or a float.
        ZeroDivisionError: If div is equal to 0.

    """
    # Evaluate that matrix data type and its elements are list, int or float
    error = 'matrix must be a matrix (list of lists) of integers/floats'
    if isinstance(matrix, list) is not True or len(matrix) == 0:
        raise TypeError(error)
    for item in matrix:
        if isinstance(item, list) is not True or len(item) == 0:
            raise TypeError(error)
        for element in item:
            if type(element) not in (int, float):
                raise TypeError(error)
    # Evaluate that the length of every list inside the matrix are equal
    for i in range(len(matrix)):
        if len(matrix[0]) != len(matrix[i]):
            raise TypeError('Each row of the matrix must have the same size')
        else:
            continue
    # Evaluate that div data type is int or float and is not zero
    if type(div) not in (int, float):
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')
    # Division between dividends and divisor (elem of the list and div)
    new_matrix = []
    for item in matrix:
        new_list = []
        for number in item:
            result = number / div
            new_list.append(round(result, 2))
        new_matrix.append(new_list)
    return new_matrix
