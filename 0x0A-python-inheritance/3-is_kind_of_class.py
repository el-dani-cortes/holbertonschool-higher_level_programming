#!/usr/bin/python3
"""Module that check the instance of a object"""


def is_kind_of_class(obj, a_class):
        """Method checks if a object is instance of a class.

        Args:
           obj: Any kind of object.
           a_class: The class to check the instance.

        Return:
             returns True if the object is an instance of,
             or if the object is an instance of a class that
             inherited from, the specified class ; otherwise False.

        """
        return isinstance(obj, a_class)
