#!/usr/bin/python3
"""Module function that creates an Object from a “JSON file"""
import json


def load_from_json_file(filename):
    """ Function that creates an Object from a “JSON file”

    Args:
       filename: Name of the JSON file.

    Return:
       A python object.

    """

    with open(filename, mode='r') as f:
        json_string = f.read()
        my_obj = json.loads(json_string)
    return my_obj
