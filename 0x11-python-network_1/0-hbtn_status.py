#!/usr/bin/python3
""" a python script that fetches from a url """
import urllib.request


if __name__ == '__main__':
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print('Body response:')
        print('\t- type: {}\n\t- content: {}\n\t- utf8 content: {}'.format(
              type(content), content, content.decode('utf-8')))
