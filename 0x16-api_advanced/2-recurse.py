#!/usr/bin/python3
"""query an api and return a list containing the titles
       of all the articles given
"""

import requests


def recurse(subreddit, hot_list=[]):
    """query an api and return a list containing the titles
       of all the articles given
    """
    url = 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)
    user_agent = 'Mozilla/5.0'
    headers = {'User-Agent': user_agent}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None

    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for child in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
