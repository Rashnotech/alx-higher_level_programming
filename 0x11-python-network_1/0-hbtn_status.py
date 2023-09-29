#!/usr/bin/python3
""" a python script that fetches from a url """
import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    content = response.read()
    print('Body response:')
    print('\t- type:{}\n\t- content: {}\n\t- utf8 content: {}'.format(
          type(content), content, content, content.decode('utf-8')))
