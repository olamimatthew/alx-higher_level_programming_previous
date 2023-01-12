#!/usr/bin/python3
"""
Module that contains function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """
    Function that writes a string to a text file
    """
    with open(filename, mode='w', encoding="utf-8") as fname:
        return fname.write(text)
