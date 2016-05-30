from __future__ import print_function

import sys
import time

from pprint import pprint

import requests


GITHUB = 'https://api.github.com'

def gh(uri):
    return '{0}/{1}'.format(GITHUB, uri)

def new_getter(token = None):
    headers = {}
    if token:
        headers = { 'Authorization': 'token %s' % token }

    def getter(url):
        return requests.get(url, headers=headers)

    def getter_with_wait(url):
        r = getter(url)
        try:
            r.raise_for_status()
        except:
            if r.status_code == 403:
                wait(r.headers['X-RateLimit-Reset'])
                r = getter(url)
                r.raise_for_status()
            else:
                raise
        return r

    return getter_with_wait

def wait(reset):
    reset = int(reset)
    while True:
        now = int(time.time() - 1)
        secs = max(reset - now, 0)
        print('wait for reset: %s s remaiting' % secs, file=sys.stderr)
        time.sleep(1)

def main(getter):
    url = gh('users?per_page=100')
    while True:
        us, url = users(getter, url)
        for u in us:
            for r in starred(getter, u):
                print('%s,%s' % (u, r))

def users(getter, url):
    r = getter(url)
    names = [ u['login'] for u in r.json() ]
    nexturl = r.links.get('next', {}).get('url', '')
    return (names, nexturl)

def starred(getter, user):
    r = getter(gh('users/%s/starred?sort=created&per_page=100' % user))
    return [repo['full_name'] for repo in r.json()]

def rate_limit(getter):
    r = getter(gh('rate_limit'))
    core = r.json()['resources']['core']
    return (core['limit'], core['remaining'], core['reset'])

if __name__ == '__main__':
    token = raw_input('Personal access token: ')
    print('')
    main(new_getter(token))
