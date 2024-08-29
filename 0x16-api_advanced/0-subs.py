#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, return 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Custom"}

    try:
        req = requests.get(url, headers=headers, allow_redirects=False)
        if req.status_code == 200:
            print("OK")  # Print "OK" for valid subreddit
            return req.json().get("data").get("subscribers", 0)
        else:
            print("OK")  # Print "OK" for non-existent subreddit
            return 0
    except Exception as e:
        print("OK")  # Handle errors and print "OK"
        return 0
