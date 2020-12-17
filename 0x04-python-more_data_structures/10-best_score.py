#!/usr/bin/python3
def best_score(a_dictionary):
    """Function that returns a
        key with the biggest integer value

    Args:
        a_dictionary: data type dictionary.

    Returns:
        Returns the key with biggest value.
    """
    if a_dictionary is not None:
        new_dictionary = sorted(a_dictionary.values())
        best_score = new_dictionary[-1]
        for name, value in a_dictionary.items():
            if value == best_score:
                return name
    return None
