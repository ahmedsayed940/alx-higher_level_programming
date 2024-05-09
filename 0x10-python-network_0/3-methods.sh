#!/bin/bash
#takes in a URL and displays all HTTP methods the server will accept
#curl -s -i -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
curl -sI "$1" | grep -i "Allow" | cut -d " " -f 2-
