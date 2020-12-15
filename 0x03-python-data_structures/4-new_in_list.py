#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """function that replaces an element
       in a list at a specific position
       without modifying the original list

    Args:
        my_list: list with elements to copy
        idx: index of element to change
        element: element to change in the copy

    Returns:
        Return copy of the original list. Or
        original list if idx is negative or
        major of the element on the list.
    """
    copy_list = my_list.copy()
    n = 0
    for item in copy_list:
        if n == idx:
            copy_list[idx] = element
            return copy_list
        n = n + 1
    return my_list
