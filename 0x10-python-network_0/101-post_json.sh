#!/bin/bash
# a bash script that send JSON POST request
curl -s -X POST --upload-file $2 $1
