#!/usr/bin/python3

""" a module that append string to text file """


def append_write(filename="", text=""):
    """ a function that appends a string at the end of a text file
        Return:
            number of characters added
    """
    count = 0
    with open(filename, 'a', encoding="utf-8") as file:
        for char in text:
            file.write(char)
            count += 1
        return count
