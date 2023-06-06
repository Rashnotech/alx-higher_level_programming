#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        x = ord(letter)
        if x >= 97 and x <= 122:
            print('{}'.format(chr(x - 32)), end="")
        else:
            print('{}'.format(letter) end="")
