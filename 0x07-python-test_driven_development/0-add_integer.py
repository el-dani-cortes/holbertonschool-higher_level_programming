#!/usr/bin/python3
"""Module to add to value int or float"""


def add_integer(a, b=98):
    """Function to add to integers or float variable

    Args:
       a(int or float): Value #1 to add.
       b(int or float): Value #2 to add.

    Returns:
       Result of the add of the two given value.

    Raises:
        TypeError: if a and b are not integer or float data types.

    """
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
