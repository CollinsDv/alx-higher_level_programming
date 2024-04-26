#!/usr/bin/python3
"""module: 3-error_code
    takes in a URL, sends a request to the URL and displays
    the body of the response(decoded in utf-8).

        - You have to manage urllib.error.HTTPError exceptions and
          print: Error code: followed by the HTTP status code
        - You must use the packages urllib and sys
        - You are not allowed to import other packages than urllib and sys
        - You don’t need to check arguments passed to the script
          (number or type)
        - You must use the with statement
"""
import urllib.request
import sys
from urllib.error import HTTPError

# use context manager to open a link
if __name__ == '__main__':
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            body = response.read()
    except HTTPError as e:
        print('Error code:', e.status)
    else:
        print(body)
