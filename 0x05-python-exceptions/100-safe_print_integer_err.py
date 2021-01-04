#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """Function that prints an integer.
    Args:
        value: data of any type (integer, string, etc.).
    Returns:
        True if value has been correctly printed.
        Otherwise, returns False.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False
