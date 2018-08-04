import math

class Ride:
    
    MINIMUM_TIME=60
    INITIAL_COST = 1
    PER_MINUTE = 0.15
    def __init__(self, bird_id, user_id):
        self.bird_id = bird_id
        self.user_id = user_id
        self.start_position = None
        self.end_position = None
        self.distance = 0
        self.cost = 0
        self.start_time = 0
        self.end_time = 0
        
    def start_ride(self, start_position, start_time):
        self.start_position = start_position
        self.end_position = start_position
        self.start_time = start_time
        self.end_time = start_time
        self.distance = 0
        self.cost = 0
    
    def end_ride(self, end_position, end_time):
        self.end_position = end_position
        self._calc_distance()
        self.end_time = end_time
        self.cost = self._calc_cost()
    
    @staticmethod
    def calc_distance(start_position, end_position):
        x_diff = (end_position[0] - start_position[0])**2
        y_diff = (end_position[1] - start_position[1])**2
        return math.sqrt(x_diff + y_diff)
    
    def _calc_distance(self):
        self.distance = Ride.calc_distance(self.start_position, self.end_position)
    
    def _calc_cost(self):
        diff = self.end_time - self.start_time
        if (diff < Ride.MINIMUM_TIME):
            return 0
        cost = Ride.INITIAL_COST
        dm = divmod(diff, 60)
        cost += dm[0] * Ride.PER_MINUTE
        cost += Ride.PER_MINUTE if dm[1] > 0 else 0
        return cost   
    
    def get_distance(self):
        return self.distance
    
    def get_cost(self):
        return self.cost
