#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit
"""
from urllib import request
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    user = {"User-Agent": "mozilla"}
    params = {"count": count, "after": after}
    request = requests.get('https://www.reddit.com/r/{}/hot.json'
                           .format(subreddit), headers=user,
                           allow_redirects=False, params=params)
    if request.status_code == 200:
        info = request.json().get('data')
        for i in info.get('children'):
            hot_list.append(i.get('data').get('title'))
    elif request.status_code != 200:
        return None
    if not info.get('data'):
        return hot_list

    return recurse(subreddit, hot_list, info.get('after'))
