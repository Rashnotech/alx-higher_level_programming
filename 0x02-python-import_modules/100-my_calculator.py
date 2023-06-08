#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div

args = sys.argv[:4]
arg = len(args)
if arg < 3:
    print('{} <a> <operator> <b>'.format(args[0]))
    sys.exit(1)
a = int(args[1])
ops = args[2]
b = int(args[3])
if __name__ == '__main__':
    if ops == "+":
        print('{} {} {} {} {}'.format(a, "+", b, "=", add(a, b)))
    elif ops == "-":
        print('{} {} {} {} {}'.format(a, "-", b, "=", sub(a, b)))
    elif ops == "*":
        print('{}{}'.format(a, b))
        print('{} {} {} {} {}'.format(a, "*", b, "=", mul(a, b)))
    elif ops == "/":
        print('{} {} {} {} {:.0f}'.format(a, "/", b, "=", div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
