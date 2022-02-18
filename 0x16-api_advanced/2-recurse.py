#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit
"""


def recurse(subreddit, hot_list=[], count=0, after=None):
    """
    Write a recursive function that queries the Reddit API and returns
    a list containing the titles of all hot articles for a given subreddit
    """
    import requests

    user = {"User-Agent": "mozilla"}
    params = {"count": count, "after": after}
    request = requests.get('https://www.reddit.com/r/{}/hot.json'
                           .format(subreddit), headers=user,
                           allow_redirects=False, params=params)
    if request.status_code == 200:
        info = request.json()
        info = info.get('data')
        for i in info.get('children'):
            hot_list.append(i.get('data').get('title'))
    if request.status_code != 200:
        return None
    if not info.get('after'):
        return hot_list

    return recurse(subreddit, hot_list, info.get('after'))
