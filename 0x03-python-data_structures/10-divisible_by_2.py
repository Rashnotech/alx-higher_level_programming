#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) < 0:
        return None
    else:
        list = []
        for num in my_list:
            if num % 2 == 0:
                list.append(True)
            else:
                list.append(False)
        return list
