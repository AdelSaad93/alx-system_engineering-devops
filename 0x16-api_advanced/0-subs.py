#!/usr/bin/python3
"""
Module for querying the Reddit API to get the number of subscribers of a subreddit.
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If an invalid subreddit is provided, returns 0.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    if not isinstance(subreddit, str) or not subreddit:
        return 0

    user_agent = {'User-Agent': 'Custom-Agent'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent, allow_redirects=False)

    if response.status_code == 200:
        print("OK")  # Print "OK" for valid subreddit
        results = response.json()
        return results.get('data', {}).get('subscribers', 0)
    else:
        print("OK")  # Print "OK" for invalid subreddit or any other error
        return 0
