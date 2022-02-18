#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.
    """
    import requests

    user = {"User-Agent": "Mozilla"}
    request = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'.
                           format(subreddit), headers=user,
                           allow_redirects=False)
    if request.status_code == 404:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in request.json().get("data").get("children")]
