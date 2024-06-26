#!/usr/bin/python3
"""module: 6-post_email
     takes in a URL and an email address, sends a POST request to the passed
     URL with the email as a parameter, and finally
     displays the body of the response.
        - The email must be sent in the variable email
        - You must use the packages requests and sys
        - You are not allowed to import packages other than requests and sys
        - You don’t need to error check arguments passed to the script
          (number or type)
"""
import sys
import requests

if __name__ == '__main__':
    response = requests.post(
            sys.argv[1], data={'email': sys.argv[2]})

    print(response.text)
