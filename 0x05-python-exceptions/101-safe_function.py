#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Function that executes a function safely.
    Args:
        fct: Always a pointer to a function.
        *args: Arguments of the function.
    Returns:
         Result of the function.
    """
    try:
        return fct(*args)
    except BaseException as err:
        print("Exception: {}".format(err), file=sys.stderr)
    else:
        return None
