#!/usr/bin/python3

import requests


def number_of_subscribers(subreddit):
    headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0)\
                    Gecko/20100101 Firefox/80.0' +
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36\
                    (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
            }
    req = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit),
                       headers=headers,
                       allow_redirects=False)

    if req.status_code != 200:
        return (0)

    json = req.json()
    d = json.get('data', {})
    return (d.get('subscribers', 0))
