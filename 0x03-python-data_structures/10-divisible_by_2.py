#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Function that finds all multiples of 2 in a list.

    Args:
        my_list: list with numbers to evaluate.

    Returns:
        Return new list with True or False,
        depending on whether the integer at
        the same position in the original list is a multiple of 2.
    """
    if my_list:
        evaluate = []
        for item in my_list:
            if item % 2 == 0:
                evaluate.append(True)
            else:
                evaluate.append(False)
        return evaluate
