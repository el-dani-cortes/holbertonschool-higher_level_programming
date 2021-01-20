#!/usr/bin/python3
"""Module that read a file"""


def read_file(filename=""):
    """Method that reads a file and prints to stdout

    Args:
       filename: name of the file to read.

    Return:
       Always nothing.

    """
    with open(filename, mode='r', encoding='utf-8') as f:
        text = f.read()
        print(text, end='')
