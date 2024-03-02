#!/usr/bin/python3
"""ython script that takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user with
the letter as a parameter."""
if __name__ == "__main__":
    import requests
    from sys import argv
    if len(argv) == 1:
        letter = ""
    else:
        letter = argv[1]
    data = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
