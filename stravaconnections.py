import json



class StravaConnection:
    def __init__(self):
        self.client_id = None
        self.client_secret = None
        self.init_strava_app_data()


    # Load data from strava_data file (sensitive data)
    def init_strava_app_data(self):
        with open('strava_data.json', 'r') as file:
            strava_app_data = json.load(file)
            self.client_id = strava_app_data['client_id']
            self.client_secret = strava_app_data['client_secret']


