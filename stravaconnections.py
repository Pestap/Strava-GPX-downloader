import json
import time

import requests
# TODO LIST:
# - find out how long is the authorization code valid (would prefer to authorize every use)
# - save token as object field
# - saving in file not needed
# - every request check if token valid, if not refresh it
# - functions for sending requests (just for sending, not constructing (that will be done by a separate module))
# - the other module for constructing requests

class StravaConnection:
    def __init__(self):
        self.__client_id = None
        self.__client_secret = None
        self.redirect_uri = 'https://localhost/'
        self.init_strava_app_data()

    # Load data from strava_data file (sensitive data)
    def init_strava_app_data(self):
        with open('strava_data.json', 'r') as file:
            strava_app_data = json.load(file)
            self.__client_id = strava_app_data['client_id']
            self.__client_secret = strava_app_data['client_secret']

    def authorize(self):
        request_url = f'https://www.strava.com/oauth/authorize?client_id={self.__client_id}' \
                      f'&response_type=code&redirect_uri={self.redirect_uri}' \
                      f'&approval_prompt=force' \
                      f'&scope=profile:read_all,activity:read_all'

        print("Click here to allow the app to gather your data: " + request_url)
        code = input("Please enter the code visible in your browser: ")

        token = self.request_token(code)
        # TODO: check if valid
        self.save_token_to_file(token)

    def request_token(self, code):
        response = requests.post(url='https://www.strava.com/api/v3/oauth/token',
                              data={'client_id': self.__client_id,
                                    'client_secret': self.__client_secret,
                                    'code': code,
                                    'grant_type': 'authorization_code'})
        return response

    def refresh_token(self):
        token = self.read_token_from_file()
        refresh_token = token['refresh_token']
        response = requests.post(url='https://www.strava.com/api/v3/oauth/token',
                                 data={'client_id': self.__client_id,
                                       'client_secret': self.__client_secret,
                                       'grant_type': 'refresh_token',
                                       'refresh_token': refresh_token})
        return response

    @staticmethod
    def check_if_token_valid(strava_token):
        return False if strava_token['expires_at'] < time.time() else True

    @staticmethod
    def save_token_to_file(token):
        with open('strava_token.json', 'w') as out:
            json.dump(token.json(), out)

    @staticmethod
    def read_token_from_file():
        with open('strava_token.json', 'r') as file:
            token = json.load(file)
            return token
