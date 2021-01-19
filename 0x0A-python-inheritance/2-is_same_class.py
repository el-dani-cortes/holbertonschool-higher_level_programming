#!/usr/bin/python3
"""Module that check the instance of a object"""


def is_same_class(obj, a_class):
        """Method checks if a object is instance of a class.

        Args:
           obj: Any kind of object.
           a_class: The class to check the instance.

        Return:
            returns True if the object is exactly an instance
            of the specified class ; otherwise False.

        """
        if type(obj) is a_class:
                return True
        else:
                return False
