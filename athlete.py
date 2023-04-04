from athletestats import AthleteStats
from stravaathleterequests import StravaAthleteRequest

class Athlete:
    def __init__(self, info: str):
        self.id = info['id']
        self.username = info['username']
        self.firstname = info['firstname']
        self.lastname = info['lastname']
        self.sex = info['sex']
        self.country = info['country']
        self.stats = None
        self.activities = list()

    def __str__(self) -> str:
        return f"{self.username}: {self.firstname} {self.lastname}, {self.country}"

    def get_stats(self, stats: str):
        self.stats = AthleteStats(stats)

    def get_activities(self) -> list[dict]:
        return self.get_athlete_activities(self)