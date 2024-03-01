#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response
(decoded in utf-8)
"""
if __name__ == "__main__":
    from sys import argv
    import urllib.request
    import urllib.parse
    data = {'email': argv[2]}
    data_url = urllib.parse.urlencode(data).encode('ascii')
    request = urllib.request.Request(argv[1], data_url)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
