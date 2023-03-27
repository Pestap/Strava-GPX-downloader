
class AthleteStats:
    def __init__(self, json: str):
        self.all_rides = json['all_ride_totals']
        self.all_runs = json['all_run_totals']
        self.all_swims = json['all_swim_totals']
        self.longest_ride = json['biggest_ride_distance']
        self.json = json

    def __str__(self):
        #return  f"All rides distance: {self.all_rides['distance'] / 1000} km\n" \
        #        f"All runs distance: {self.all_runs['distance'] / 1000} km\n" \
         #       f"All swims distance: {self.all_swims['distance']} m"
        return self.json.__str__()