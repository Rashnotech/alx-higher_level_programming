#!/usr/bin/python3
"""a python script that takes request to the URL and display"""
import urllib.request
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    with urllib.request.urlopen(url) as response:
        header = response.getheader("X-Request-Id")
        print(header)
