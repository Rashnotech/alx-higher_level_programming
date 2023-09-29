#!/usr/bin/python3
""" a python script that takes URL and send post request"""
import requests
from sys import argv


url = argv[1]
email = argv[2]
data = {'email': email}
response = requests.get(url, data=data)
