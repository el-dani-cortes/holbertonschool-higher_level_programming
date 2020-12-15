#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Function that deletes the item at a specific position in a list.

    Args:
        my_list: list with items.
        idx: index of the list to remove.

    Returns:
        Return a the list without the item removed.
    """
    if my_list:
        n = 0
        if idx > 0 or idx < len(my_list):
            for item in my_list:
                if n == idx:
                    del my_list[idx]
                n = n + 1
            return my_list
        else:
            return my_list
