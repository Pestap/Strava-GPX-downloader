import json
import requests
from stravaconnections import StravaConnection


# get list of activities in json format
def get_activities_of_type(activity_type: str) -> [str]:
    access_token = load_tokens('strava_data.json')[0]
    activities_url = f"https://www.strava.com/api/v3/athlete/activities?" \
                  f"access_token={access_token}"
    # TODO: authorization (https://www.grace-dev.com/python-apis/strava-api/)
    return requests.get(activities_url).json()

a = StravaConnection()
a.authorize()