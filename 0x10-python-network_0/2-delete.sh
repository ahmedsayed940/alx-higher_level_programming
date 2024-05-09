#!/bin/bash
# sends a DELETE request to the URL and displays the body of a response
response=$(curl -s -X DELETE "$1")
echo "$response"
