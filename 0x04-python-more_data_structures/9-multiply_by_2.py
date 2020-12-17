#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Function that returns a new
       dictionary with all values multiplied by 2.

    Args:
        a_dictionary: data type dictionary.

    Returns:
        Returns a new dictionary.
    """
    new_dictionary = {}
    for key, value in a_dictionary.items():
        new_dictionary[key] = value * 2
    return new_dictionary
