#!/usr/bin/python3

import requests


def top_ten(subreddit):
    """prints top 10 posts for a given subbreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    user_agent = 'Mozilla/5.0'
    headers = {'user_agent': user_agent}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print('None')
        return

    results = response.json()['data']
    [print(c.get("data").get("title")) for c in results.get("children")]
