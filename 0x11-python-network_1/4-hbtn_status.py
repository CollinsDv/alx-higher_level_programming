#!/usr/bin/python3
"""module: 4-hbtn_status
    fetches https://alx-intranet.hbtn.io/status
        - You must use the package requests
        - You are not allow to import packages other than requests
        - The body of the response must be display like the following example
        (tabulation before -)
        guillaume@ubuntu:~/0x11$ ./4-hbtn_status.py | cat -e
        Body response:$
            - type: <class 'str'>$
            - content: OK$
"""
import requests
# if __name__ == '__main__':
response = requests.get('https://alx-intranet.hbtn.io/status')
print('Body response:')
print('\ttype:', type(response.text))
print('\tcontent', response.text)
