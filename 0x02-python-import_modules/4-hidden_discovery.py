#!/usr/bin/python3

if __name__ == '__main__':
    module = dir("hidden_4")
    for name in module:
        if name[:2] != '__':
            print('{}'.format(name))
