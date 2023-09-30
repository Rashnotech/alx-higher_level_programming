#!/usr/bin/python3
"""a python script that takes request to the URL and display"""
import requests
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    response = requests.get(url)
    head = response.headers["X-Request-Id"]
    print(head)
