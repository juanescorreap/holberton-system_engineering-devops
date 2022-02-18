#!/usr/bin/python3
"""
function that queries the Reddit API and returns
the number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    user = {"User-Agent": "Mozilla"}
    request = requests.get('https://www.reddit.com/r/{}/about.json'.
                           format(subreddit), headers=user,
                           allow_redirects=False)
    if request.status_code == 200:
        return request.json().get('data').get('subscribers')
    else:
        return 0
