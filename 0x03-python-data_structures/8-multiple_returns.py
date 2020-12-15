#!/usr/bin/python3
def multiple_returns(sentence):
    """ Function that returns a tuple
        with the length of a string and its first character.

    Args:
        sentence: string

    Returns:
        Return lenght and first character of sentence.
    """
    if len(sentence) == 0:
        tuple_sentence = (0, None)
    else:
        tuple_sentence = (len(sentence), sentence[0])
    return tuple_sentence
