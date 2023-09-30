#!/usr/bin/python3
""" a python script that takes URL and send post request"""
import urllib.request
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    email = argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data=data) as response:
        body = response.read().decode('utf-8')
        print(body)
