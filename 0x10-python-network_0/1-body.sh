#!/bin/bash
# a bash script that takes in a URL, sends a GET request to the URL, and displays the body of the reponse
curl -s -o -w "%{http_code}" $1
