#!/usr/bin/python3

""" a module that read text file """


def read_file(filename=""):
    with open(filename, encoding="UTF-8") as file:
        for content in file:
            print(content, end='')
