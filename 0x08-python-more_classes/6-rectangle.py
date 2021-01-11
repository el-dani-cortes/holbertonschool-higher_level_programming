#!/usr/bin/python3
"""Module that defines a class rectangle"""


class Rectangle:
    """Class that defines a rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Init method to initialized a instance"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Method that calculates area of a rectangle.

        Args:
            Not arguments.

        Return:
            Area value of the rectangle.

        """
        Rectangle.number_of_instances += 1
        return self.__width * self.__height

    def perimeter(self):
        """Method that calculates perimeter of a rectangle.

        Args:
            Not arguments.

        Return:
            Perimeter value of the rectangle.

        """
        Rectangle.number_of_instances += 1
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """Method that returns a rectangle by # character.

        Args:
            Not arguments.

        Return:
            A rectangle represented by character #.

        """
        hash_line = '#' * self.__width
        rectangle = (hash_line + '\n') * (self.__height - 1) + hash_line
        Rectangle.number_of_instances += 1
        return rectangle

    def __repr__(self):
        """Method that returns a formal
           representation of a instance.

        Args:
            Not arguments.

        Return:
            Formal representation of a object instance.

        """
        Rectangle.number_of_instances += 1
        representation = "Rectangle({}, {})".format(
            self.__width, self.__height)
        return representation

    def __del__(self):
        """Method that deletes a object.

        Args:
            Not arguments.

        Return:
            Always nothing.

        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
