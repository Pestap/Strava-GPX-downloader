from athletestats import AthleteStats


class Athlete:
    def __init__(self, info: str):
        print(info)
        input()
        self.id = info['id']
        self.username = info['username']
        self.firstname = info['firstname']
        self.lastname = info['lastname']
        self.sex = info['sex']
        self.country = info['country']
        self.stats = None

    def __str__(self) -> str:
        return f"{self.username}: {self.firstname} {self.lastname}, {self.country}"

    def get_stats(self, stats: str):
        self.stats = AthleteStats(stats)

