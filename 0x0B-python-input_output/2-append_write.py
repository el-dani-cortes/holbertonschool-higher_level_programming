#!/usr/bin/python3
"""Module that apppend into a file"""


def append_write(filename="", text=""):
    """Method that creates and appends a string to a file.

    Args:
       filename: name of the file to read.
       Text: The string to append in the file.

    Return:
       The numbers of characters written.

    """
    with open(filename, mode='a', encoding='utf-8') as f:
        num_characters = f.write(text)
    return num_characters
