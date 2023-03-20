import json
import requests


# load Strava API tokens from file
def load_tokens(filename: str) -> (str,str):
    with open(filename, 'r') as file:
        tokens = json.load(file)
        return tokens['access_token'], tokens['refresh_token']


# Get athlete info in json format
def get_athlete() -> str:
    access_token = load_tokens('strava_tokens.json')[0]
    athlete_url = f"https://www.strava.com/api/v3/athlete?" \
                  f"access_token={access_token}"

    return requests.get(athlete_url).json()


print(get_athlete()['firstname'])