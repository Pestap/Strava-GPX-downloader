import json
import requests


# load Strava API tokens from file
def load_tokens(filename: str) -> (str,str):
    with open(filename, 'r') as file:
        tokens = json.load(file)
        return tokens['access_token'],tokens['refresh_token']



