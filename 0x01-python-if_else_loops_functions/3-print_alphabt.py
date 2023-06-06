#!/usr/bin/python3
for x in range(ord('a'), ord('z')+1):
    if chr(x) == 'e' or chr(x) == 'q':
        continue
    print('{}'.format(chr(x)), end="")
