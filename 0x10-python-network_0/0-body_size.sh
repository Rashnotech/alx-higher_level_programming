#!/bin/bash
# a bash script that takes in a URL, sends a request to that URL and 
# displays the size of the body of the response
if [[ $# -ne 1 ]]; then
	echo "Usage: ./0-body_size.sh port"
else
	curl -s $1 | wc -c
fi
