#!/usr/bin/python3

import sys

args = sys.argv[1:]
arg = len(args)
ret = 0
for i in range(arg):
    ret += int(args[i])
if __name__ == '__main__':
    print('{}'.format(ret))
