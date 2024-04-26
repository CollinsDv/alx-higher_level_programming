#!/usr/bin/python3
"""module: 2-post_email.py
    takes in a URL and an email, sends a POST request to the passed URL with the email
    as a parameter, and displays the body of the response (decoded in utf-8)
        - The email must be sent in the email variable
        - You must use the packages urllib and sys
        - You are not allowed to import packages other than urllib and sys
        - You don’t need to check arguments passed to the script (number or type)
        - You must use the with statement
"""
import urllib.request
import urllib.parse
import sys

# use context manager to open a link
if __name__ == '__main__':
    payload = {'email': sys.argv[2]}
    formated_payload = urllib.parse.urlencode(payload)
    payload_data = formated_payload.encode('utf-8')

    with urllib.request.urlopen(sys.argv[1], data=payload_data) as response:
        email = response.read()
        # get character encoding style
        encoding = response.headers.get_content_charset()
        # decode
        decoded_email = email.decode(encoding)
        print(decoded_email)
