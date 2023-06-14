#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delete = []
    for key, item in a_dictionary.items():
        if item == value:
            delete.append(key)
    for d in delete:
        del a_dictionary[d]
    return a_dictionary
