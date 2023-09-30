#!/usr/bin/python3
"""a pyscript that takes GitHub credential and display id"""
import requests
from sys import argv


if __name__ == '__main__':
    user = argv[1]
    pwd = argv[2]
    req = requests.get('https://api.github.com/user', auth=(user, pwd))
    response = req.json()
    if response == {}:
        print('None')
    else:
        print(response.get('id'))
