#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Function that replaces an element
    of a list at a specific position

    Args:
        my_list: list with elements
        idx: index of the list to replace
        element: element value to replace

    Returns:
        Return my_list list.
    """
    n = 0
    for item in my_list:
        if n == idx:
            my_list[idx] = element
            return my_list
        n = n + 1
    return my_list
