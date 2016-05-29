# -*- coding: utf-8 -*-

import requests

GITHUB = 'https://api.github.com'

class Requester(object):
    def __init__(self, token=None):
        """if token is None, just make requests unauthorized"""
        if token:
            self.headers = { 'Authorization': 'token %s' % token }
        else:
            self.headers = {}

    def get(self, uri):
        url = '{github}{uri}'.format(github=GITHUB, uri=uri)
        return requests.get(url, headers=self.headers)

if __name__ == '__main__':
    r = Requester()
    print r.get('/rate_limit').json()
