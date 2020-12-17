#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Function that prints a dictionary by ordered keys.

    Args:
        a_dictionary: data type dictionary.

    Returns:
        Always nothing.
    """
    for key in sorted(a_dictionary.keys()):
        print("{:s}: {}".format(key, a_dictionary[key]))
