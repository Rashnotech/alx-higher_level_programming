#!/bin/bash
# a bash script that send a GET request to the URL and displays the body
curl -s -X GET -H 'X-School-User-Id: 98' $1
