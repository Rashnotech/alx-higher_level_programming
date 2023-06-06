#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        x = ord(letter)
        if x >= 97 and x <= 122:
            x -= 32
            letter = chr(x)
        print('{}'.format(letter), end="")
    print()
