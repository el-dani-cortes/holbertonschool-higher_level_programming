#!/usr/bin/python3
"""Module that check the instance of a object"""


def inherits_from(obj, a_class):
        """Method checks if a object is an instance
           of a class that inherited (directly or indirectly)
           from the specified classof a class.

        Args:
           obj: Any kind of object.
           a_class: The class to check the instance.

        Return:
           Returns True if the object is an instance of
           a class that inherited (directly or indirectly)
           from the specified class; otherwise False.

        """
        if type(obj) is a_class:
                return False
        else:
                return issubclass(type(obj), a_class)
