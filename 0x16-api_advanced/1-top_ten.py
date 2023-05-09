#!/usr/bin/python3
"""1-top_ten.py"""
import requests

def top_ten(subreddit):
    """prints top 10 titles"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers = headers)

    if response.status_code != 200:
        print(None)
        return
    posts = response.json()['data']['children']
    for post in posts:
        print(post['data']['title'])
