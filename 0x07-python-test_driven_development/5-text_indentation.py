#!/usr/bin/python3
"""Module function that prints a text with 2 new lines
   after each of these characters: ., ? and :"""


def text_indentation(text):
    """Function that function that prints a text with 2 new lines
       after each of these characters: ., ? and :.

    Args:
       text(str): Text to print with the new requirement.

    Returns:
       Always Nothing.

    Raises:
        TypeError: If text is not a str data type

    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    i = 0
    text = text.strip(' ')
    while i < len(text):
        print(text[i], end='')
        if text[i] in (".", "?", ":"):
            print('\n')
            if (i + 1) < len(text):
                while text[i + 1] == " ":
                    i += 1
        i += 1
