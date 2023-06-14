#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [new_arr if val == search else val for val in my_list]
