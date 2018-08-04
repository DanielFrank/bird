from models.ride import Ride

class Bird:
    
    def __init__(self, bird_id, drop_position):
        self.id = bird_id
        self.drop_position = drop_position
        self.current_position = drop_position
        self.ride = None
        self.longest_wait = 0
        self.last_ride_end_time = 0
        self.total_distance = 0
        
    def start_ride(self, user_id, start_position, start_time):
        ride = Ride(self.id, user_id)
        ride.start_ride(start_position, start_time)
        self.ride = ride
        self.current_position = start_position
        if (self.last_ride_end_time > 0):
            this_wait = start_time - self.last_ride_end_time
            if (this_wait > self.longest_wait):
                self.longest_wait = this_wait
        return self.ride
    
    def end_ride(self, end_position, end_time):
        self.last_ride_end_time = end_time
        self.current_position = end_position
        ride = self.ride
        ride.end_ride(end_position, end_time)
        self.total_distance += ride.get_distance()
        return ride
    
    def get_total_distance(self):
        return self.total_distance
    
    def get_longest_wait(self):
        return self.longest_wait
    
    def get_distance_from_drop_position(self):
        return Ride.calc_distance(self.drop_position, self.current_position)
    
