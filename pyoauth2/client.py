# -*- coding: utf-8 -*-

__author__ = "Yoshifumi YAMAGUCHI <@ymotongpoo>"

__all__ = ['OAuth2AuthenticationFlow',
           'Storage',
           'FileStorage', 
           'OAuth2APIRequest']

import requests

from urllib import urlencode
import json
import os
import os.path
import webbrowser


REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'

class Storage(object):
    """ Base storage class for storing credentials
    """
    def __init__(self):
        self.elements = [
            'access_token',
            ]
    
    def get(self):
        """ Return access token
        """
        pass

    def save(self, data):
        """ Store access token into storage
        """
        pass


class FileStorage(Storage):
    """ Storage class using Shelve
    """
    def __init__(self, filename):
        Storage.__init__(self)
        self.filename = filename
        self.elements = [unicode(e) for e in self.elements]

        
    def get(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as f:
                try:
                    data = json.load(f)
                    return data
                except ValueError, e:
                    return None
        else:
            return None

    
    def save(self, data):
        stored_data = {}
        if os.path.exists(self.filename):
            fpr = open(self.filename, 'r+')
            try:
                stored_data = json.load(fpr)
            except ValueError, e:
                raise ValueError(e)
            else:
                fpr.close()
        
        for e in self.elements:
            stored_data[e] = data[e]
        fpw = open(self.filename, 'w+')
        json.dump(stored_data, fpw)
        
            

class OAuth2AuthorizationFlow(object):
    """ OAuth 2.0 authorization class
    """

    def __init__(self, required_params,
                 extra_auth_params=None,
                 extra_token_params=None,
                 **kwargs):

        """
        Args:
          required_params: dictionary including required parameters
        """
        self.client_id = required_params['client_id']
        self.client_secret = required_params['client_secret']
        self.auth_uri = required_params['auth_uri']
        self.token_uri = required_params['token_uri']
        self.redirect_uri = required_params['redirect_uri']

        if isinstance(extra_auth_params, dict):
            self._extra_auth_params = extra_auth_params
        else:
            self._extra_auth_params = {}

        if isinstance(extra_token_params, dict):
            self._extra_token_params = extra_token_params
        else:
            self._extra_token_params = {}
        
        if 'scope' in required_params.keys():
            self.scope = ' '.join(required_params['scope'])
        else:
            self.scope = None

        self.authorization_code = None
        self.access_token = None

        self.base_headers = requests.defaults.defaults['base_headers']


    def retrieve_authorization_code(self):
        """ retrieve authorization code to get access token
        """
        
        request_param = {
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            }

        if self.scope:
            request_param['scope'] = self.scope

        if self._extra_auth_params:
            request_param.update(self._extra_auth_params)

        r = requests.get(self.auth_uri, params=request_param,
                         allow_redirects=False)
        url = r.headers.get('location') 
        webbrowser.open_new_tab(url)

        authorization_code = raw_input("Code: ")
        if self.validate_code(authorization_code):
            self.authorization_code = authorization_code

        
    def retrieve_token(self):
        """ retrieve access token with code fetched via 
        retrieve_authorization_code method.
        """

        if self.authorization_code:
            request_param = {
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "redirect_uri": self.redirect_uri,
                "code": self.authorization_code
                }

            print request_param, urlencode(request_param)

            if self._extra_token_params:
                request_param.update(self._extra_token_params)

            content_length = len(urlencode(request_param))
            headers = {
                'Content-Length': str(content_length),
                'Content-Type': 'application/x-www-form-urlencoded'
                }
        
            r = requests.post(self.token_uri, data=request_param,
                              headers=headers)
            jsondata = json.loads(r.text)
            self.access_token = jsondata
            return self.access_token

        else:
            print "authorization code is required before getting accesss token"
            print "Please call retrieve_authorization_code() beforehand"


    def validate_code(self, code):
        return True



class OAuth2APIRequest(object):
    """ Base class for OAuth 2.0 API request
    """
    def __init__(self, access_token):
        self.access_token = access_token
        self.authorization_header = {
            "Authorization": "OAuth %s" % str(self.access_token)
            }

    def request(self, url, extra_headers={}):
        headers = {}
        headers.update(self.authorization_header)
        headers.update(extra_headers)

        params = {
            "oauth_token": self.access_token
            }

        r = requests.get(url, params=params, headers=headers)
        return r.text
