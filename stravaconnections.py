import json
import time

import requests

# This module is responsible for user authorization and request sending
# NOT for constructing request


class StravaConnection:
    def __init__(self):
        self.__client_id = None
        self.__client_secret = None
        self.__token = None
        self.redirect_uri = 'https://localhost/'
        self.init_strava_app_data()

    # Load data from strava_data file (sensitive data)
    def init_strava_app_data(self):
        with open('strava_data.json', 'r') as file:
            strava_app_data = json.load(file)
        self.__client_id = strava_app_data['client_id']
        self.__client_secret = strava_app_data['client_secret']
        self.authorize()

    def authorize(self):
        request_url = f'https://www.strava.com/oauth/authorize?client_id={self.__client_id}' \
                      f'&response_type=code&redirect_uri={self.redirect_uri}' \
                      f'&approval_prompt=force' \
                      f'&scope=profile:read_all,activity:read_all'

        print("Click here to allow the app to gather your data: " + request_url)
        code = input("Please enter the code visible in your browser: ")

        self.request_token(code)

    def request_token(self, code):
        response = requests.post(url='https://www.strava.com/api/v3/oauth/token',
                              data={'client_id': self.__client_id,
                                    'client_secret': self.__client_secret,
                                    'code': code,
                                    'grant_type': 'authorization_code'})
        self.save_token(response)
        StravaConnection.save_token_to_file(response)

    def refresh_token(self):
        refresh_token = self.__token['refresh_token']
        response = requests.post(url='https://www.strava.com/api/v3/oauth/token',
                                 data={'client_id': self.__client_id,
                                       'client_secret': self.__client_secret,
                                       'grant_type': 'refresh_token',
                                       'refresh_token': refresh_token})
        self.save_token(response)
        StravaConnection.save_token_to_file(response)

    # Saves token in memory as json
    def save_token(self, new_token):
        self.__token = new_token.json();

    # Checks if token is valid
    def check_if_token_valid(self):
        if self.__token is None:
            return False
        elif self.__token['expires_at'] < time.time():
            return False
        else:
            return True

    # Sends a request by adding access_token and refreshing it if needed
    def send_request(self, url: str) -> str:
        # refresh token if needed
        if not self.check_if_token_valid():
            self.refresh_token()

        # check if url ends with ?
        if url[-1] != "?":
            url += "?"

        # add authentication token to request
        request_url = url + f"access_token={self.__token['access_token']}"

        return requests.get(request_url).json()

    @staticmethod
    def save_token_to_file(token):
        with open('strava_token.json', 'w') as out:
            json.dump(token.json(), out)

    @staticmethod
    def read_token_from_file():
        with open('strava_token.json', 'r') as file:
            token = json.load(file)
            return token
