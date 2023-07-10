#!/usr/bin/python3

""" Single inheritance """


class MyList(list):
    """ a class that inherits from another class """

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
