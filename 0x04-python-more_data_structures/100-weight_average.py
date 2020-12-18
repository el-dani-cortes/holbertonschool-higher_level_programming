#!/usr/bin/python3
def weight_average(my_list=[]):
    """Function that converts a Roman numeral to an integer.

    Args:
        roman_string: string with roman number.

    Returns:
        Returns a integer.
    """
    sum_weighted = 0
    division_sum = 0
    if my_list:
        for items in my_list:
            sum_weighted += items[0] * items[1]
            division_sum += items[1]
        result = sum_weighted / division_sum
        return result
    return 0
