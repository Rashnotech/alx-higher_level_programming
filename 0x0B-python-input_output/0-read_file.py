#!/usr/bin/python3

""" a module that read text file """


def read_file(filename=""):
    """ a function that reads a text file and print """
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end='')
