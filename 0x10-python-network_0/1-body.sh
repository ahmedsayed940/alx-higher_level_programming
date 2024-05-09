#!/bin/bash
#sends a GET request to the URL, and displays the body of the response
# Display only body of a 200 status code response
curl -sX GET "$1" -L 200
