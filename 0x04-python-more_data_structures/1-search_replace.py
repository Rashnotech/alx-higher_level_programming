#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(my_list)
    size = len(my_list)
    if size != 0:
        for i in my_list:
            if new_list[i] == search:
                new_list[i] = replace
    return new_list
