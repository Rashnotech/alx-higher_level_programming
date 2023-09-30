#!/usr/bin/python3
"""a pyscript that takes in a letter and sends a POST request to url"""
import requests
from sys import argv


if __name__ == '__main__':
    letter = argv[1] if len(argv) > 1 else ""
    data = {'q': letter}
    req = requests.post('http://0.0.0.0:5000/search_user', data=data)
    response = req.json()
    try:
        if response:
            print('[{}] {}'.format(response.id, response.name))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
