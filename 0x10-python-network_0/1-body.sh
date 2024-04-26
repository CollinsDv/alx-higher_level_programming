#!/bin/bash
# takes in a URL, sends a GET request to the URL, and displays the body of the response
# 	Display only body of a 200 status code response
#	You have to use curl
curl -X GET -sL $1
