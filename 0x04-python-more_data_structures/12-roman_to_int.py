#!/usr/bin/python3
def roman_to_int(roman_string):
    digit = 0
    r_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'XL': 40
              'M': 1000, 'D': 500, 'C': 100, 'IX': 9, 'XC': 90
              'CM': 900, 'CL': 150, 'CD': 400}
    if len(roman_string) == 0 or roman_string.isalpha():
        upper = roman_string.upper()
        for num in upper:
            if num in r_dict.keys():
                digit += r_dict[num]
    return digit
