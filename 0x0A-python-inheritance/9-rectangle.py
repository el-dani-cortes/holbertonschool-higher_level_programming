#!/usr/bin/python3
"""Module that defines a class Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
        """Define a class Rectangle that inherits from BaseGeometry"""

        def __init__(self, width, height):
                """Method that init a rectangle object.

                Args:
                   width: Size of the rectangle's width.
                   height: Size of the rectangle's height.

                Return:
                   Always nothing.

                """
                self.integer_validator("width", width)
                self.integer_validator("height", height)
                self.__width = width
                self.__height = height

        def area(self):
                """Method that returns the area of a rectangle"""
                return (self.__width * self.__height)

        def __str__(self):
                """Method that returns a specific string.

                Args:
                   Not arguments.

                Return:
                   A specific string: [Rectangle] <width>/<height>.

                """
                return "[Rectangle] {}/{}".format(self.__width, self.__height)
