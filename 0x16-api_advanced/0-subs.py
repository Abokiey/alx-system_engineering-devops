#!/usr/bin/python3

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    user_agent = 'Mozilla/5.0'
    headers = {'User-Agent': user_agent}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    results = response.json()["data"]["subscribers"]
    return results