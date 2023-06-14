#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if len(my_list) == 0:
        return my_list
    else:
        return [new_arr if val == search else val for val in my_list]
