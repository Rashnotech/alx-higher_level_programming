#!/usr/bin/python3
def roman_to_int(roman_string):
    digit = []
    if not roman_string or not roman_string.isalpha():
        return 0
    diction = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'M': 1000,
               'D': 500, 'C': 100}
    upper = roman_string.upper()
    for r_num in upper:
        if r_num in diction.keys():
            digit.append(diction[r_num])
    num = 0
    size = len(digit)
    for i in range(size):
        if i < size - 1 and digit[i] < digit[i+1]:
            num -= digit[i]
        else:
            num += digit[i]
    return num
