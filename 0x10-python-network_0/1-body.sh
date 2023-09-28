#!/bin/bash
# a bash script that takes in a URL, sends a GET request to the URL, and
# displays the body of the reponse
if [[ $# -eq 1]]; then
	curl --get $1
else
	echo "Usage: ./1-body.sh port"
fi
