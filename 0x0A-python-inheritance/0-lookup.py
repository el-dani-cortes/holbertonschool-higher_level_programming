#!/usr/bin/python3
"""Module that returns list of available
attributes and methods of an object"""


def lookup(obj):
    """
    Method that returns all of available
    attributes and methods of an object.

    Args:
        obj: It's a any kind of obj.

    Return:
        Returns a list with attributes and methods.

    """
    return dir(obj)
