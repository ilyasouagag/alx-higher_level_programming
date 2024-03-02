#!/usr/bin/python3
"""lists the 10 most recent commits on a given GitHub repository.
"""


if __name__ == "__main__":
    import sys
    import requests
    link = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    r = requests.get(link)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
