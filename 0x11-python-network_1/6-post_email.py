#!/usr/bin/python3
""" a python script that takes URL and send post request"""
import requests
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    email = argv[2]
    data = {'email': email}
    response = requests.post(url, data=data)
    print(response)
