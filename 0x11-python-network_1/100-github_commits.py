#!/usr/bin/python3
"""
Holberton challenge: Script that displays 10 commits
(from the most recent to oldest) of the repository
"""

from sys import argv
import requests

if __name__ == "__main__":
    repo = argv[1]
    username = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(username, repo)
    response = requests.get(url)
    for commit in response.json()[:10]:
        print(
            "{}: {}".format(
                commit['sha'], commit['commit']['author']['name']
            )
        )
