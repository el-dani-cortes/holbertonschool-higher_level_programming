#!/usr/bin/python3
def element_at(my_list, idx):
    """Function that retrieves
    an element from a list.

    Args:
        my_list: list with elements
        idx: index of list to retrieve

    Returns:
        Return value in idx or None if it fails.
    """
    n = 0
    for item in my_list:
        if n == idx:
            return item
        n = n + 1
    return None
