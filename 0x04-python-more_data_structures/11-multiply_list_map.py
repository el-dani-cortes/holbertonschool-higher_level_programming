#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """ function that returns a list with all
        values multiplied by a number without using any loops.

    Args:
        my_list: List with numbers.
        number: number value to multiply the numbers in the list.

    Returns:
        Returns a new list.
    """
    return list(map(lambda x: x * number, my_list))
