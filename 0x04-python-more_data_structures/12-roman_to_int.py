#!/usr/bin/python3
def alpha(s):
    for c in s:
        if not c.isalpha():
            return 1
    return 0

def roman_to_int(roman_string):
    digit = 0
    if alpha(roman_string) == 1 or roman_string is None:
        return 0
    r_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'XL': 40, 'M': 1000,
              'D': 500, 'C': 100, 'IX': 9, 'CM': 900,
              'CD': 400, 'LC': 150, 'XC': 90}
    if len(roman_string) != 0 or alpha(roman_string) == 0:
        r_man = roman_string.upper()
        length = len(r_man)
        for i in range(length - 1):
            char = r_man[i]
            if char + r_man[i + 1] in r_dict.keys():
                digit += r_dict[char + r_man[i + 1]]
                i += 1
            elif char in r_dict.keys():
                digit += r_dict[char]
        if length != 2 and r_man[-1] in r_dict.keys():
            digit += r_dict[r_man[-1]]
            return digit
