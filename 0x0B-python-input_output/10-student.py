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

    def to_json(self, attrs=None):
        """Method that retrieves a dictionary
           representation of the object.

        Args:
           attrs: List of attributes to retrieves.

        Return:
           A dictionary with attributes of the objects

        """
        if type(attrs) is list:
            attrs_dict = {}
            attributes = self.__dict__
            for item in attrs:
                try:
                    attrs_dict[item] = attributes[item]
                except KeyError:
                    pass
            return (attrs_dict)
        else:
            return (self.__dict__)
