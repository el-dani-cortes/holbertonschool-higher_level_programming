#!/usr/bin/python3
def number_keys(a_dictionary):
    """Function that returns the
        number of keys in a dictionary.

    Args:
        a_dictionary: data type dictionary.

    Returns:
        Number of keys in the dictionary.
    """
    number_of_keys = len(list(a_dictionary.keys()))
    return number_of_keys
