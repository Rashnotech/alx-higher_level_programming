#!/usr/bin/python3
"""a python script that takes request to the URL and display"""
import requests
from sys import argv


url = argv[1]
response = requests.get(url)
head = response.headers["X-Request-Id"]
print(head)
