#!/usr/bin/python3
"""Module that defines a class Mylist"""


class MyInt(int):
    """Class that defines a new kind of int inherits from superclass int"""

    def __init__(self, value):
        """Method that initializes a MyInt object

        Args:
           Value(int): Integer value.

        Return:
           Always nothing.

        """
        super().__init__()

    def __eq__(self, other):
        """Method that inverted the standard method __eq__

        Args:
           Other(int): Integer value to compare

        Return:
           True when are diferent and False when are equal.

        """
        return int(self) != other

    def __ne__(self, other):
        """Method that inverted the standard method __ne__

        Args:
           Other(int): Integer value to compare

        Return:
           True when are equal and False when are diferents.

        """
        return int(self) == other
