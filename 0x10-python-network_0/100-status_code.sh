#!/bin/bash
# a bash script that displays status code
curl -s -o /dev/null -w '%{response_code}' $1
