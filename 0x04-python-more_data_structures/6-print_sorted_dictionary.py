#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    diction_copy = a_dictionary.copy()
    for key, values in sorted(diction_copy.items()):
        print('{}: {}'.format(key, values))
