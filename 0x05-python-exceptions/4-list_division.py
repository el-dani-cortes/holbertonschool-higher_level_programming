#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Function that divides element by element 2 lists.
    Args:
        my_list_1: List with dividend element of division.
        my_list_2: List with divisor element of division.
        list_length: Length of the new list with division result.
    Returns:
        A new list (length = list_length) with all divisions.
    """
    list_result = []
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        finally:
            list_result.append(result)
    return list_result
