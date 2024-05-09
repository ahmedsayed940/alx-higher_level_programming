#!/bin/bash
#sends a GET request to the URL, and displays the body of the response
# Display only body of a 200 status code response
curl -s -w "\n%{http_code}" "$1" | awk 'END {if ($1 == 200) print}'
