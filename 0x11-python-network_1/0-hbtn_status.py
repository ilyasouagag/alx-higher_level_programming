#!/usr/bin/python3
"""
This Python script demonstrates how to fetch
the content of a URL using the urllib.request
module. The script makes a GET request to the URL
"https://alx-intranet.hbtn.io/status" and prints
information about the response.
"""
if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as link:
        response = link.read()
        print("Body response:")
        print(f"\t- type: {type(response)}")
        print(f"\t- content: {response}")
        print(f"\t- utf8 content: {response.decode("utf-8")}")
