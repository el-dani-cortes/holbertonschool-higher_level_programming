#!/usr/bin/python3
def safe_print_division(a, b):
    """Function that divides 2 integers and prints the result.
    Args:
        a: Dividend element of division.
        b: Divisor element of division.
    Returns:
        The value of the division, otherwise: None
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
