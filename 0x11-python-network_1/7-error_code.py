#!/usr/bin/python3
"""a python script that takes URL, and displays the response"""
import requests
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    body = requests.get(url)
    if body.status_code >= 400:
        print('Error code: {}'.format(body.status_code))
    else:
        print(body.text)
