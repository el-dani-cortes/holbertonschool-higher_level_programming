#!/usr/bin/python3
def no_c(my_string):
    """function that removes all
       characters c and C from a string

    Args:
        my_string: string to change

    Returns:
        Return new string.
    """
    copy_string = ""
    for letter in my_string:
        if letter != "c" and letter != "C":
            copy_string = copy_string + letter
    return (copy_string)
