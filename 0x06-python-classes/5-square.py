#!/usr/bin/python3


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

    def my_print(self):
        """Method that prints in stdout the square
           with the character #

        Args:
           Any Arguments

        Returns:
           Always nothing.

        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("{}".format('#' * self.__size))

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
