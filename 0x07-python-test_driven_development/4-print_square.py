#!/usr/bin/python3
"""Module that prints a square with the character #"""


def print_square(size):
    """Function that prints a square with the character #.

    Args:
       size(int): Size of the square.

    Returns:
       Always Nothing.

    Raises:
        TypeError: if size is not a integer and if size is a float
                   and less than zero.
        ValueError: If size is less than zero.

    """
    if (type(size) is float and size < 0) or type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print('#' * size)
