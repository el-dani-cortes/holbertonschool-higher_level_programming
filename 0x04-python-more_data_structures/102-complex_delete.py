#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """ Function that deletes keys
        with a specific value in a dictionary.

    Args:
        a_dictionary: data type dictionary

    Returns:
        Returns a new dictionary
    """
    del_list = []
    for key, element in a_dictionary.items():
        if value == element:
            del_list.append(key)
    for item in del_list:
        del a_dictionary[item]
    return a_dictionary
