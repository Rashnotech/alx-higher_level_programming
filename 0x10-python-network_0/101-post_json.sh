#!/bin/bash
# a bash script that send JSON POST request
curl -s -X POST -d "$@2" $1
