#!/usr/bin/python3
"""Module that write into a file"""


def write_file(filename="", text=""):
    """Method that creates and write a text in a file.

    Args:
       filename: name of the file to read.
       Text: The string to write in the file.

    Return:
       The numbers of characters written.

    """
    with open(filename, mode='w', encoding='utf-8') as f:
        num_characters = f.write(text)
    return num_characters
