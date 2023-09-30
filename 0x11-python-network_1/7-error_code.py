#!/usr/bin/python3
"""a python script that takes URL, and displays the response"""
import requests
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    try:
        body = requests.get(url)
        print(body)
    except requests.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
