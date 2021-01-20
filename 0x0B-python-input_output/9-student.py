#!/usr/bin/python3
"""Module that defines a class"""


class Student:
    """Defines a student class"""

    def __init__(self, first_name, last_name, age):
        """Method that initiliazed a student class

        Args:
           first_name: first name of the student.
           last_name: last name of the student.
           age: age of the student.

        Return:
           Always nothing.

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method that retrieves a dictionary
           representation of the object.
        """
        return (self.__dict__)
