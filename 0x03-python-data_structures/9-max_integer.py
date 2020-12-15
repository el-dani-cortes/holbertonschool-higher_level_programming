#!/usr/bin/python3
def max_integer(my_list=[]):
    """Function that finds the biggest integer of a list

    Args:
        my_list: list with numbers to evaluate

    Returns:
        Return the biggest integer of a list.
        None if list is empty.
    """
    my_list.sort()
    return(my_list[-1])
