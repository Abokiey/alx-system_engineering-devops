#!/usr/bin/python3

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)

    user_agent = 'Mozilla/5.0'
    headers = {'user-agent' : user_agent}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0

    result = response.json()['data']['subscribers']
    return result
