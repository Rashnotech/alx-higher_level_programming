#!/usr/bin/python3
def no_c(my_string):
    element = ""
    for i in range(len(my_string)):
        if my_string[i] in ["c", "C"]:
            element += " "
        else:
            element += my_string[i]
    return element
