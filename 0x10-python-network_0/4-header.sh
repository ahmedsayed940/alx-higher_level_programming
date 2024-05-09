#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
	    echo "Usage: $0 <URL>"
	        exit 1
fi

# Send GET request to the URL with the specified header and display the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
