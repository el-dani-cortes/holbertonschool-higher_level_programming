#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """function that replaces or adds key/value in a dictionary.

    Args:
        a_dictionary: data type dictionary.
        key: key to search in the dictionary.
        value: value to create or for replace.

    Returns:
        Returns a modified dicitonary.
    """
    a_dictionary[key] = value
    return a_dictionary
