
class AthleteStats:
    def __init__(self, json: str):
        self.all_rides = json['all_ride_totals']
        self.all_runs = json['all_run_totals']
        self.all_swims = json['all_swim_totals']
        self.longest_ride = json['biggest_ride_distance']

    def __str__(self):
        return  f"All rides: {self.all_rides}" \
                f"All runs: {self.all_runs}" \
                f"All swims: {self.all_swims}"