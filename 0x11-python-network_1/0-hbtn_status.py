#!/usr/bin/python3
"""A script that
- fetches https://alx-intranet.hbtn.io/status.
- uses urlib package
"""
if __name__ == '__main__':
    import urllib.request
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as link:
        response = link.read()
        print("Body response:")
        print("\t- type: {}".format(type(response)))
        print("\t- response: {}".format(response))
        print("\t- utf8 response: {}".format(response.decode('utf-8')))
