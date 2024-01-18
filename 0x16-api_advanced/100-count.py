#!/usr/bin/python3
import re
import requests
"""parse titles of all hot articles and print the
       sorted count
    """


def add_title(dictionary, hot_posts):
    """ Adds items into a list """
    if len(hot_posts) == 0:
        return

    title = hot_posts[0]['data']['title'].split()
    for word in title:
        for key in dictionary.keys():
            c = re.compile("^{}$".format(key), re.I)
            if c.findall(word):
                dictionary[key] += 1

    hot_posts.pop(0)
    add_title(dictionary, hot_posts)


def recurse(subreddit, dictionary, after=None):
    """parse titles of all hot articles and print the
       sorted count
    """
    u_agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': u_agent
    }

    params = {
        'after': after
    }
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    dic = response.json()
    hot_posts = dic['data']['children']
    add_title(dictionary, hot_posts)
    after = dic['data']['after']
    if not after:
        return
    recurse(subreddit, dictionary, after=after)


def count_words(subreddit, word_list):
    """ Init function """
    dictionary = {}

    for word in word_list:
        dictionary[word] = 0

    recurse(subreddit, dictionary)

    lst = sorted(dictionary.items(), key=lambda kv: kv[1])
    lst.reverse()

    if len(lst) != 0:
        for item in lst:
            if item[1] != 0:
                print("{}: {}".format(item[0], item[1]))
    else:
        print("")
