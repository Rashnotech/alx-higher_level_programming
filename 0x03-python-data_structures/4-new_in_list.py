#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    size = len(my_list)
    if idx < 0 or idx > size or size == 0:
        return (my_list)
    else:
        list = my_list.copy()
        list[idx] = element
        return (list)
