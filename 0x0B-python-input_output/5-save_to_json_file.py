#!/usr/bin/python3
"""Module that function that returns the JSON
   representation of an object (string)"""
import json


def save_to_json_file(my_obj, filename):
    """ Function that writes an Object to a text file,
        using a JSON representation

    Args:
       my_obj: object to convert to JSON string.
       filename: Name of the file to create.

    Return:
       Always nothing.

    """

    json_string = json.dumps(my_obj)
    with open(filename, mode='w') as f:
        f.write(json_string)
