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
    if request.status_code >= 400:
        return None

    h_list = hot_list + [child.get("data").get("title")
                         for child in request.json()
                         .get("data")
                         .get("children")]

    info = request.json()
    if info.get("data").get("after") is None:
        return h_list

    return recurse(subreddit, h_list, info.get("data").get("count"),
                   info.get("data").get("after"))
