#!/usr/bin/python3
def search_replace(my_list, search, replace):
    lists = my_list.copy()
    if search == 0 or search >= len(lists):
        return lists
    lists[search - 1] = replace
    return lists

