#!/usr/bin/python3
"""Module that defines a class rectangle"""


class Rectangle:
    """Class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Init method to initialized a instance"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Method getter for width atributte

        Args:
            Not arguments

        Return:
            The current value of the width atributte

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Method setter for width atributte

        Args:
            value(int): width value of the rectangle

        Return:
            Always nothing

        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Method getter for height atributte

        Args:
            Not arguments

        Return:
            The current value of the height atributte

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Method setter for height atributte

        Args:
            value(int): height value of the rectangle

        Return:
            Always nothing

        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
