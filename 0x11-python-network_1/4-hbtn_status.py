#!/usr/bin/python3
""" a python script that fetches from a url """
import requests


response = requests.get('https://alx-intranet.hbtn.io/status')
print('Body response:')
print('\t- type: {}\n\t- content: {}'.format(
      type(response.text), response.text))
