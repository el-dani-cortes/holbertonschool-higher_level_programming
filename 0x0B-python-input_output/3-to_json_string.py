#!/usr/bin/python3
"""Module that function that returns the JSON
   representation of an object (string)"""
import json


def to_json_string(my_obj):
    """Function that returns the JSON
       representation of an object (string).

    Args:
       my_obj: object to convert to JSON string.

    Return:
       A JSON string.

    """
    return (json.dumps(my_obj))
