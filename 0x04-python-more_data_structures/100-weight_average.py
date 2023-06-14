#!/usr/bin/python3
def weight_average(my_list=[]):
    avg, div = 0, 0
    if len(my_list) != 0:
        for tuples in my_list:
            if len(tuples) == 1:
                tuples += (0, 0)
            avg += tuples[0] * tuples[1]
            div += tuples[1]
        avg /= div
    return avg
