#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Class that defines a square"""
    def __init__(self, size=0):
        """Method for initialize a square object.

        Args:
            size(int): Size of the side of the square.

        """
        self.__size = size
