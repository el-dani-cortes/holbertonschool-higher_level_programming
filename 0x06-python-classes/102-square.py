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
        self.size = size

    def area(self):
        """Method that calculate the area of a square.

        Args:
           Any Arguments

        Returns:
           The current square area.

        """
        return (self.__size) ** 2

    @property
    def size(self):
        """Getter of size

        Args:
           Any Arguments

        Returns:
           The current value of size.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter of size

        Args:
           value(int): Size of the side of the square.

        Return:
           Always nothing

        """
        if isinstance(value, int) is True:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')


    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()
