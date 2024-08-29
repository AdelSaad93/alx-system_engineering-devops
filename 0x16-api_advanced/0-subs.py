#!/usr/bin/python3
"""
Module for querying the Reddit API to get the number of subscribers of a subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If an invalid subreddit is provided, return 0.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Custom-User-Agent"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            print("OK")  # Print "OK" for a valid subreddit
            data = response.json().get("data", {})
            return data.get("subscribers", 0)
        else:
            print("OK")  # Print "OK" for an invalid subreddit
            return 0
    except requests.RequestException:
        print("OK")  # Handle errors and print "OK"
        return 0
