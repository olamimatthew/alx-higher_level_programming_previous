#!/usr/bin/python3
"""
Module that contains a function to open text file
"""


def read_file(filename=""):
    """
    function that opens a text file
    """
    with open(filename, mode='r', encoding="utf-8") as fname:
        print(fname.read(), end="")
