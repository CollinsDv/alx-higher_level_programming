#!/usr/bin/python3
"""module: 8-json_api
    takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user
    with the letter as a parameter.
        - The letter must be sent in the variable q
        - If no argument is given, set q=""
        - If the response body is properly JSON formatted and not empty,
          display the id and name like this: [<id>] <name>
        Otherwise:
        - Display Not a valid JSON if the JSON is invalid
        - Display No result if the JSON is empty
        - You must use the package requests and sys
        - You are not allowed to import packages other than requests and sys
"""
import sys
import requests

if __name__ == '__main__':
    if len(sys.argv) > 1:
        param = {'q': sys.argv[1]}
    else:
        param = {'q': ""}
    response = requests.post(
            "http://0.0.0.0:5000/search_user", data=param)
    if response.status_code == 200:
        try:
            data = response.json()
            if data:
                print('[{}] {}'.format(data['id'], data['name']))
            else:
                print('No result')
        except json.JSONDecodeError:
            print('Not a valid JSON')
    else:
        print('No result')
