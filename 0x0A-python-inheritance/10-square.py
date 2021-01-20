#!/usr/bin/python3
"""Module that defines a class geometry"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
        """Class that defines a Square class"""

        def __init__(self, size):
                """Method that init a square object.

                Args:
                   size(int): Size of the square's width.

                Return:
                   Always nothing.

                """
                self.integer_validator(str(size), size)
                self.__size = size
                super().__init__(size, size)

        def area(self):
                """Method that returns the area of a square"""
                return super().area()
