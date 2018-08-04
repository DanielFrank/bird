class User:
    
    def __init__(self, user_id):
        self.id = user_id
        self.total_spent = 0
        self.num_rides = 0
    
    def add_completed_ride(self, ride):
        self.num_rides += 1
        self.total_spent += ride.get_cost()
    
    def get_total_spent(self):
        return self.total_spent
    
    def get_num_rides(self):
        return self.num_rides
