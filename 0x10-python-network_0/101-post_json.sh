#!/bin/bash
# a bash script that send JSON POST request
curl -s -X POST -H "Content-Type: application/json" -d "$(cat $2)" $1
