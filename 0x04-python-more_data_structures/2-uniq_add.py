#!/usr/bin/python3
def uniq_add(my_list=[]):
    x = 0
    for num in set(my_list):
        x += num
    return x

