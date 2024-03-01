#!/usr/bin/python3
"""
This Python script demonstrates how to fetch
the content of a URL using the urllib.request
module. The script makes a GET request to the
URL "https://alx-intranet.hbtn.io/status" and
prints information about the response.
"""
if __name__ == '__main__':
    import urllib.request
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as link:
        response = link.read()
        print("Body response:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(response.decode('utf-8')))
