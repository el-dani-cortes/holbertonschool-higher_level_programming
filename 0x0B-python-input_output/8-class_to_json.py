#!/usr/bin/python3
"""Module returns the dictionary description
   with simple data structure.
"""
import json


def class_to_json(obj):
    """ Function that returns dictionary description with simple data structure
        (list, dictionary, string, integer and boolean) for JSON
        serialization of an object.

    Args:
       obj: Instance of a Class.

    Return:
       Dictionary description with simple data structure
       (list, dictionary, string, integer and boolean)

    """
    return obj.__dict__
