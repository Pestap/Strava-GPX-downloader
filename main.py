from stravaathleterequests import StravaAthleteRequest

request = StravaAthleteRequest()
request.get_current_athlete()
print(request.athlete)

print(request.get_athlete_activities())
