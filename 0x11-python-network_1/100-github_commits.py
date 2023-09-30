#!/usr/bin/python3
"""a pyscript that print commit of a repository"""
import requests
from sys import argv


if __name__ == '__main__':
    name = argv[1]
    repo = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(name, repo)
    req = requests.get(url)
    res = req.json()
    try:
        for i in range(10):
            print('{}: {}'.format(res[i].get('sha'), res[i].get('commit')
                                  .get('author').get('name')))
    except Exception:
        pass
