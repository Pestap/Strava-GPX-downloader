import json
import requests


# load Strava API tokens from file
def load_tokens(filename: str) -> (str,str):
    with open(filename, 'r') as file:
        tokens = json.load(file)
        return tokens['access_token'], tokens['refresh_token']


# Get athlete info in json format
def get_athlete() -> str:
    access_token = load_tokens('strava_data.json')[0]
    athlete_url = f"https://www.strava.com/api/v3/athlete?" \
                  f"access_token={access_token}"

    return requests.get(athlete_url).json()


# get list of activities in json format
def get_activities_of_type(activity_type: str) -> [str]:
    access_token = load_tokens('strava_data.json')[0]
    activities_url = f"https://www.strava.com/api/v3/athlete/activities?" \
                  f"access_token={access_token}"
    # TODO: authorization (https://www.grace-dev.com/python-apis/strava-api/)
    return requests.get(activities_url).json()

print(get_activities_of_type("asd"))