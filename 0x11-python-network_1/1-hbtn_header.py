#!/usr/bin/python3
import urllib.request
import sys

url = sys.argv[1]

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    x_request_id = response.getheader('X-Request-Id')

print(x_request_id)
