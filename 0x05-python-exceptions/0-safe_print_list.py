#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Function that prints x elements of a list
    Args:
        my_list: List with elements to print.
        x: Represents the number of elements to print.
    Returns:
        The number of elements printed.
    """
    count = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end='')
            count += 1
        except IndexError:
            pass
    print()
    return count
