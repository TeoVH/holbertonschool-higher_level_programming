#!/usr/bin/python3
"""
Script that sends a POST request to the passed URL with
the email as a parameter, and displays the body of the response
"""

from urllib import request, parse, response
import sys

if __name__ == "__main__":
    data = parse.urlencode({"email": sys.argv[2]}).encode()
    with request.urlopen(sys.argv[1], data) as response:
        print(response.read().decode('utf-8'))
