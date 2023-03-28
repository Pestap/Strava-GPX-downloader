from stravaathleterequests import StravaAthleteRequest

request = StravaAthleteRequest()
request.get_current_athlete()
print(request.athlete)

result = request.get_athlete_activities()
print(result)
print(len(result))
