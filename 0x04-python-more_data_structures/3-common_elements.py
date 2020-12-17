#!/usr/bin/python3
def common_elements(set_1, set_2):
    """function that returns a set
       of common elements in two sets.

    Args:
        set_1: data type set #1.
        set_2: data type set #2.

    Returns:
        Common elements in two sets.
    """
    set_common = set_1 & set_2
    return set_common
