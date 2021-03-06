#!/usr/bin/python3
"""Module that defines a class rectangle"""


class Rectangle:
    """Class that defines a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

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
        if self.width == 0 or self.height == 0:
            return ""
        else:
            hash_line = str(self.print_symbol) * self.width
            rectangle = (hash_line + '\n') * (self.height - 1) + hash_line
        return rectangle

    def __repr__(self):
        """Method that returns a formal
           representation of a instance.

        Args:
            Not arguments.

        Return:
            Formal representation of a object instance.

        """
        representation = "Rectangle({}, {})".format(
            self.width, self.height)
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Method compare areas between rectangles.

        Args:
            Rect_1(object): Instance of the rectangle object.
            Rect_2(object): Instance of the rectangle object.

        Return:
            The instance with the biggest area.

        """
        if isinstance(rect_1, Rectangle) is not True:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if isinstance(rect_2, Rectangle) is not True:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
