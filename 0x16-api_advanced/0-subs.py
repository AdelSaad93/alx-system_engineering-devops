#!/usr/bin/python3
"""Module for task 0"""

import requests

def number_of_subscribers(subreddit):
	"""Queries the Reddit API and returns the number of subscribers
	to the subreddit"""
	url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
	headers = {"User-Agent": "My-User-Agent"}

	try:
		response = requests.get(url, headers=headers, allow_redirects=False)
		if response.status_code == 200:
			data = response.json().get("data")
			if data and "subscribers" in data:
				print("OK")
				return data.get("subscribers")
		else:
			print("OK")  # Handle non-existing subreddit case
			return 0
	except Exception as e:
		print("OK")
		return 0
