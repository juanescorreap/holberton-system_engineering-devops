#!/usr/bin/python3
"""
function that queries the Reddit API and returns
the number of subscribers for a given subreddit
"""


def number_of_subscribers(subreddit):
    import requests
    request = requests.get('https://www.reddit.com/r/{}/about.json'.
                           format(subreddit), allow_redirects=False)
    if request.status_code == 200:
        return request.json().get('data').get('subscribers')
    else:
        return 0
