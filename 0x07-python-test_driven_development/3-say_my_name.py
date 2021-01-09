#!/usr/bin/python3
"""Module to print your first and lastname"""


def say_my_name(first_name, last_name=""):
    """Function that prints first and last name.

    Args:
       first_name(str): First name string.
       last_name(str): Last name string.

    Returns:
       Always nothing.

    Raises:
        TypeError: if first_name or last_name are not string data type.

    """
    if isinstance(first_name, str) is not True:
        raise TypeError('first_name must be a string')
    if isinstance(last_name, str) is not True:
        raise TypeError('last_name must be a string')
    print('My name is {:s} {:s}'.format(first_name, last_name))
