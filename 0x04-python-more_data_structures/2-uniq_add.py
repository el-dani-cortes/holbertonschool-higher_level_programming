#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Function that adds all unique integers
       in a list (only once for each integer).

    Args:
        my_list: is the initial list.

    Returns:
        Sum of all unique numbers integers in the list.
    """
    sum = 0
    set_unique = set(my_list)
    for item in set_unique:
        sum += item
    return sum
