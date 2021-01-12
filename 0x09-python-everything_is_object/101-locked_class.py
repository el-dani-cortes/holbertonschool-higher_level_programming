#!/usr/bin/python3
"""Module that defines a locked class"""


class LockedClass:
    """Class that defines that prevents the user from
       dynamically creating new instance attributes, except
       if the new instance attribute is called first_name.

    """
    __slots__ = ['first_name']
