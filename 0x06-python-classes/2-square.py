#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Class that defines a square"""
    def __init__(self, size=0):
        """Method for initialize a square object
           with validation of the data type of size variable.

        Args:
            size(int): Size of the side of the square.

        """
        if isinstance(size, int) is True:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')
