#!/usr/bin/python3
"""Module that defines a class rectangle"""


class Rectangle:
    """Class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Init method to initialized a instance.

        Args:
           width(int): Size of the width of the rectangle.
           height(int): Size of the height of the rectangle.

        Return:
            The current value of the width atributte.

        """
        self.width = width
        self.height = height

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

    def area(self):
        """Method that calculates area of a rectangle.

        Args:
            Not arguments.

        Return:
            Area value of the rectangle.

        """
        return self.width * self.height

    def perimeter(self):
        """Method that calculates perimeter of a rectangle.

        Args:
            Not arguments.

        Return:
            Perimeter value of the rectangle.

        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    def __str__(self):
        """Method that returns a rectangle by # character.

        Args:
            Not arguments.

        Return:
            A rectangle represented by character #.

        """
        hash_line = '#' * self.width
        rectangle = (hash_line + '\n') * (self.height - 1) + hash_line
        return rectangle

    def __repr__(self):
        """Method that returns a rectangle by # character.

        Args:
            Not arguments.

        Return:
            A rectangle represented by character #.

        """
        representation = "Rectangle({}, {})".format(
            self.width, self.height)
        return representation
