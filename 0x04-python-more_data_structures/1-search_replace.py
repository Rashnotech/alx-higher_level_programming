#!/usr/bin/python3
def search_replace(my_list, search, replace):
    lists = my_list.copy()
    if len(my_list) == 0:
        for i in my_list:
            if i == search:
                lists[search] = replace
    return lists
