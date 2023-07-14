#!/usr/bin/python3

""" a module that inserts a line of text to a file """


def append_after(filename="", search_string="", new_string=""):
    """ a function that inserts a line of text to a file 
        Args:
            filename: the name of the file
            search_string: the search string
            new_string: string to replace with
    """
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
        file.truncate()
