#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Function that prints the first x elements of a list and only integers.
    Args:
        my_list: A list of elements of any data type.
        x: The number of elements to access in my_list.
    Returns:
        The real number of integers printed.
    """
    count = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end='')
            count += 1
        except (TypeError, ValueError):
            pass
    print()
    return count
