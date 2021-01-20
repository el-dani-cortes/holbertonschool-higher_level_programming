#!/usr/bin/python3
"""Module that defines a class geometry"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
        """Defines a Square class"""

        def __init__(self, size):
                """Method that init a square object.

                Args:
                   size(int): Size of the square's width.

                Return:
                   Always nothing.

                """
                self.integer_validator("size", size)
                self.__size = size
                super().__init__(size, size)

        def area(self):
                """Method that returns the area of a square"""
                return super().area()

        def __str__(self):
                """Method that returns a specific string.

                Args:
                   Not arguments.

                Return:
                   A specific string: [Square] <width>/<height>.

                """

                return "[Square] {}/{}".format(self.__size, self.__size)
