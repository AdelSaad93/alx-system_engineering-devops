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
    # Set up the URL for the Reddit API request
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # Set up custom User-Agent to avoid Too Many Requests error
    headers = {"User-Agent": "Custom-User-Agent"}

    # Perform the request and disable redirects
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            # Successfully got a response, extract the number of subscribers
            data = response.json().get("data", {})
            return data.get("subscribers", 0)
        else:
            # Invalid subreddit or other errors, return 0
            return 0
    except requests.RequestException:
        # Catch any request errors and return 0
        return 0
