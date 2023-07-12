#!/usr/bin/python3

""" a module that writes to text file """


def write_file(filename="", text=""):
    """ a function that  writes a string to a text file 
        Returns:
            number of character written
    """
    count = 0;
    with open(filename, 'w', encoding="utf-8") as file:
        for line in text:
            file.write(line)
            count += 1;
        print(file.read())
    return count
