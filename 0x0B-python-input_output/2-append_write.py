#!/usr/bin/python3
"""
Module that contains function that append a string at the
end of a text file
Return the number of added character
"""


def append_write(filename="", text=""):
    """
    Function that appends a string at the end of a text file
    Returns the number of character added
    """
    with open(filename, mode='a', encoding="utf-8") as f_name:
        f_name.write(text)
    return len(text)
