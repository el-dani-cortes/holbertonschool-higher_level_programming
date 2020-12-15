#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """function that prints all integers
       of a list, in reverse order

    Args:
        my_list: list with elements

    Returns:
        Return always nothing
    """
    if my_list:
        my_list.reverse()
        for item in my_list:
            print("{:d}".format(item))
