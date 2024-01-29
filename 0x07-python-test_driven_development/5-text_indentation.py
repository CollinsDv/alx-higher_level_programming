#!/usr/bin/python3

"""
module: 5-text_indentation.py
it splits text based on certain key values
"""


def text_indentation(text):
    """print output text"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    # remove leading whitespace
    text = text.lstrip()

    i = 0
    while i < len(text):
        if text[i] in ['.', '?', ':']:
            print(text[i])
            print()
            i += 1
            if text[i] == ' ':
                i += 1
        else:
            print(text[i], end='')
            i += 1
