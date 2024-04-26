#!/usr/bin/python3
"""module: 5-hbtn_header
    takes in a URL, sends a request to the URL and displays
    the value of the variable X-Request-Id in the response header
        - You must use the packages requests and sys
        - You are not allow to import other packages than requests and sys
        - The value of this variable is different for each request
        - You don’t need to check script arguments (number and type)
"""
import requests
import sys

if __name__ == '__main__':
    response = requests.head(sys.argv[1])
    print(response.headers["X-Request-Id"])
