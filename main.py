from stravaconnections import StravaConnection


a = StravaConnection()
a.authorize()
print(a.send_request(f"https://www.strava.com/api/v3/athlete/activities?"))