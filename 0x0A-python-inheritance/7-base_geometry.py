#!/usr/bin/python3
"""Module that defines a class geometry"""


class BaseGeometry:
        """Class that defines geometry"""

        def area(self):
                """Method that raises an Exception"""
                raise Exception("area() is not implemented")

        def integer_validator(self, name, value):
                """Method that validates a value

                Args:
                   name(string): name of the value.
                   value(int): data to validate.

                Return:
                   Always nothing.

                """
                if type(value) is not int:
                        raise TypeError("{} must be an integer".format(name))
                if value <= 0:
                        raise ValueError("{} must be greater than 0".
                                         format(name))
