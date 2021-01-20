#!/usr/bin/python3
"""Module that defines a class Mylist"""


class MyList(list):
    """Class that defines a new list inherits from superclass
    list"""

    def print_sorted(self):
        """Method that prints the list, sorted (ascending sort).

        Args:
           Not arguments.

        Return:
           Always nothing.

        """
        sorted_list = sorted(self)
        print(sorted_list)
