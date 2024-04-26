#!/usr/bin/python3
"""module: 0-hbtn_status
    fetches a URL
    use only urllib package
    OUTPUT:
        Body response:
            - type: <class 'bytes'>
            - content: b'OK'
            - utf8 content: OK
"""
import urllib.request
# connect with Request object with content manager
with urllib.request.urlopen(
        'https://alx-intranet.hbtn.io/status') as response:
    # get headers alone
    body = response.read()

decoded_body = body.decode('utf-8')
print('Body response:')
print('\t- type:', type(body))
print('\t- content:', body)
print('\t- utf8 content:', decoded_body)
