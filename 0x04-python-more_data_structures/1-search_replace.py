#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """function that replaces all occurrences
       of an element by another in a new list.

    Args:
        my_list: is the initial list.
        search: is the element to replace in the list.
        replace: is the new element

    Returns:
        New list with elements replaced.
    """
    new_list = my_list.copy()
    for n, item in enumerate(new_list):
        if search == item:
            new_list[n] = replace
    return new_list
