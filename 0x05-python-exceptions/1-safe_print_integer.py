#!/usr/bin/python3
def safe_print_integer(value):
    """Function that prints an integer with "{:d}".format().
    Args:
        value: data of any type (integer, string, etc.).
    Returns:
        True if value has been correctly printed.
        Otherwise, returns False.
    """
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
