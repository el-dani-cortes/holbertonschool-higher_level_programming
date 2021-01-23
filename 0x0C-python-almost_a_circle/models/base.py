#!/usr/bin/pytho3
"""Module base"""
import json


class Base:
    """Defines a base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Method that assign the public instance attribute id

        Args:
           id(int): integer value to manage id in this project

        Return:
           Always nothing.

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Method that returns the JSON
           string representation
        """
        if list_dictionaries is None or bool(list_dictionaries) is False:
            return "[]"
        else:
            json_string = json.dumps(list_dictionaries)
            return json_string

    @classmethod
    def save_to_file(cls, list_objs):
        """ Method that writes the JSON string representation
            of list_objs to a file
        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dictionaries = []
                for obj in list_objs:
                    dictionary = obj.to_dictionary()
                    list_dictionaries.append(dictionary)
                json_string = Base.to_json_string(list_dictionaries)
                f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Method that returns the list of the
           JSON string representation
        """
        if json_string is None or bool(json_string) is False:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Update the class Base and returns a instance with all
           attributes already set

        Args:
           dictionary: Dictionary with all attributes of the object

        Return:
           A instance with all attributes already set

        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Method that returns a list of instances
           - the type of these instances depends on cls
        """
        filename = "{}.json".format(cls.__name__)
        instance_list = []
        try:
            with open(filename, 'r') as f:
                json_string = f.read()
                dictionary_list = cls.from_json_string(json_string)
                for item in dictionary_list:
                    instance = cls.create(**item)
                    instance_list.append(instance)
        except FileNotFoundError:
            return instance_list
        return instance_list
