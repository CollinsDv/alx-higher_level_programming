#!/usr/bin/python3
"""module: 1-hbtn_header
    takes in a URL, sends a request to the URL and displays the value of
    the X-Request-Id variable found in the header of the response.
        - use only urllib and sys
        - value of variable varies with each request
        - You don't need to check the number/type of args passed to script
        - must use with
"""
import urllib.request
import sys

# generate request object
# request_obj = urllib.request.Request(sys.argv[1])
# use context manager to open a link
if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        value = response.getheader('X-Request-Id')
        print(value)
