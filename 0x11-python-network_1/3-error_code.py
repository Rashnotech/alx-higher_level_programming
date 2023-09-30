#!/usr/bin/python3
"""a python script that takes URL, and displays the response"""
import urllib.request
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
