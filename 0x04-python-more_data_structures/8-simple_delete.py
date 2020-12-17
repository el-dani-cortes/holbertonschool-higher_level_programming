#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Function that deletes a key in a dictionary.

    Args:
        a_dictionary: data type dictionary.
        key: key to delete in the dictionary.

    Returns:
        Returns a modified dictionary.
    """
    if key in a_dictionary:
        del a_dictionary[key]
        return a_dictionary
    return a_dictionary
