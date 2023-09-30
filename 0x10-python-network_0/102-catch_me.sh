#!/bin/bash
# a bash script that request to an IP:port/catch_me that cause a server to respond
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
