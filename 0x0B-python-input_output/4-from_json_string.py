#!/usr/bin/python3
"""Module that  that returns an object (Python data structure)
   represented by a JSON string"""
import json


def from_json_string(my_str):
    """Function that  that returns an object
       (Python data structure) represented by a JSON string.

    Args:
       my_str: JSON string to convert to a python object.

    Return:
       A python data structure object

    """
    return (json.loads(my_str))
