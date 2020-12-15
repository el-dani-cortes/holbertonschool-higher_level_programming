#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Function that prints a list

    Args:
        my_list: list to print

    Returns:
        Always nothing.
    """
    for number in my_list:
        print("{:d}".format(number))
