# -*- coding: utf-8 -*-

from pyoauth2.client import OAuth2AuthorizationFlow, \
    FileStorage, OAuth2APIRequest
from flask import Flask, redirect, render_template, url_for, request

import json
from urlparse import urlparse, parse_qs

class YouTubeAPIRequest(OAuth2APIRequest):
    def __init__(self, access_token):
        OAuth2APIRequest.__init__(self, access_token)
        self.authorization_header = {
            "Authorization": "Bearer %s" % self.access_token
            }

yt_feed_uri = r"https://gdata.youtube.com/feeds/api/users/default/uploads?alt=json"

required_params = {
    'client_id': "XXXXXXXXXXXX.apps.googleusercontent.com",
    'client_secret': "XXXXXXXXXXXXXXXXXXXXXX",
    'auth_uri': r"https://accounts.google.com/o/oauth2/auth",
    'token_uri': r"https://accounts.google.com/o/oauth2/token",
    'scope': [r'http://gdata.youtube.com'],
    'redirect_uri': r"http://127.0.0.1:5000/callback"
    }

extra_auth_params = {
    'response_type': "code",
    'access_type': "offline"
    }

extra_token_params = {
    'grant_type': "authorization_code",
    }


app = Flask(__name__)

flow = OAuth2AuthorizationFlow(required_params,
                               extra_auth_params,
                               extra_token_params)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/redirect')
def route_to_index():
    return flow.retrieve_authorization_code(redirect_func=redirect)

    
@app.route('/callback', methods=['GET'])
def callback():
    if request.method == 'GET':
        url = urlparse(request.url)
        params = parse_qs(url[4])
        flow.set_authorization_code(params['code'][0])

        reply = flow.retrieve_token()

        req = YouTubeAPIRequest(reply[u'access_token'])
        data = req.request(yt_feed_uri)
        jsondata = json.loads(data)
        return json.dumps(jsondata, indent=2)



if __name__ == '__main__':
    app.debug = True
    app.run()
