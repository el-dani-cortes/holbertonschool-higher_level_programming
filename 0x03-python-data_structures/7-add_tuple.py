#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Function that adds 2 tuples

    Args:
        tuple_a: data type tuple a
        tuple_b: data type tuple b

    Returns:
        Return the sum of tuples with two integers
    """
    tuple_sum = (0, 0)
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    tuple_sum = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
    return tuple_sum
