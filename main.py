from stravaathleterequests import StravaAthleteRequest

request = StravaAthleteRequest()
#request.get_current_athlete()
#print(request.athlete)

#result = request.get_athlete_activities()

request.get_activities_of_type("ride")
