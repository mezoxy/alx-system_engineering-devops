#!/usr/bin/python3
'''Module 1-top_ten'''
import requests


def top_ten(subreddit):
    '''Write a function that queries the Reddit API and prints the
    titles of the first 10 hot posts listed for a given subreddit.'''
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' +
            'AppleWebKit/537.36 (KHTML, like Gecko)' +
            'Chrome/58.0.3029.110 Safari/537.3'
            }
    result = request.get(url, headers=headers, allow_redirects=False)
    if result.status_code == 404:
        return
    results = result.json().get("data", {}).get("children", [])
    [print(i.get("data", {}).get("title")) for i in results]
