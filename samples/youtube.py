# -*- coding: utf-8 -*-

from pyoauth2.client import OAuth2AuthorizationFlow, FileStorage, OAuth2APIRequest

class YouTubeAPIRequest(OAuth2APIRequest):
    def __init__(self, access_token):
        OAuth2APIRequest.__init__(self, access_token)
        self.authorization_header = {
            "Authorization": "Bearer %s" % self.access_token
            }

        

if __name__ == '__main__':

    yt_feed_uri = r"https://gdata.youtube.com/feeds/api/users/default/uploads"

    required_params = {
        'client_id': "XXXXXXXXXXXXX.apps.googleusercontent.com",
        'client_secret': "XXXXXXXXXXXXXXXXXXX",
        'auth_uri': "https://accounts.google.com/o/oauth2/auth",
        'token_uri': "https://accounts.google.com/o/oauth2/token",
        'scope': [r'http://gdata.youtube.com'],
        'redirect_uri': "urn:ietf:wg:oauth:2.0:oob"
        }

    extra_auth_params = {
        'response_type': "code",
        'access_type': "offline"
        }

    extra_token_params = {
        'grant_type': "authorization_code",
        }

    storage = FileStorage('youtube.dat')
    credentials = storage.get()
    if credentials is None:
        flow = OAuth2AuthorizationFlow(required_params,
                                       extra_auth_params,
                                       extra_token_params,
                                       True)
        flow.retrieve_authorization_code()
        credentials = flow.retrieve_token()
        storage.save(credentials)
    
    access_token = credentials['access_token']
    
    req = YouTubeAPIRequest(access_token)
    data = req.request(yt_feed_uri)
    print data

    
    
