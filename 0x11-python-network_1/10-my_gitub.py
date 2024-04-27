#!/usr/bin/python3
"""
takes your GitHub credentials
(username and password) and uses the
GitHub API to display your id
"""
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    auth = HTTPBasicAuth(username, password)
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=auth)
    print(r.json().get('id'))
