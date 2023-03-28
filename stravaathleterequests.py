from stravaconnections import StravaConnection
from stravarequests import StravaRequest
from athlete import Athlete


class StravaAthleteRequest(StravaRequest):
    def __init__(self):
        super().__init__()
        self.athlete = Athlete(self.get_current_athlete())

    def get_current_athlete(self) -> str:
        url = "https://www.strava.com/api/v3/athlete"
        return self.connection.send_request(url)

    def get_athlete_stats(self):
        url = f"https://www.strava.com/api/v3/athletes/{self.athlete.id}/stats"
        self.athlete.get_stats(self.connection.send_request(url))

    def get_athlete_activities(self):
        url = f"https://www.strava.com/api/v3/athlete/activities"
        params = {"per_page": "200",
                  "page": "1"}
        # TODO: dodać parametr na typ aktywności, albo dodatkowa funkcja
        # save all summary_polylines in file (remember to replace \\ with \)
        # save all id's
        # no way to export gpx, streams with latitude, longitude, altitude ...
        # create gpx's from that
        # or - get lat, long, alt - get middle, get middle nearest surface (overpass API), apply it for distance between two gpx points
        # from that I can gather data about surfaces
        #
        all_activities = []
        while True:
            response = self.connection.send_request(url, params)
            if len(response) == 0:
                break
            all_activities += response
            # update page number
            new_page_number = int(params['page']) + 1
            params['page'] = str(new_page_number)

        return all_activities
    