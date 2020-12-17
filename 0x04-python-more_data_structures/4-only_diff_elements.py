#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """function that returns a set of
       all elements present in only one set.

    Args:
        set_1: data type set #1.
        set_2: data type set #2.

    Returns:
        All elements present in only one set.
    """
    set_common = set_1 ^ set_2
    return set_common
