import unittest
from ..user import User
from ..ride import Ride

class UserTest(unittest.TestCase):
    def setUp(self):
        self.user_id = 1234
        self.bird_id = "ABCD"
        self.user = User(self.user_id)
        self.ride = Ride(self.bird_id, self.user_id)
    
    def test_add_completed_ride(self):
        """Add completed ride should increment the user's number of rides and add its cost to total cost"""
        self.run_the_test(0,0)
        self.set_cost(12)
        self.run_the_test(1, 12)
        self.set_cost(15)
        self.run_the_test(2, 27)

    def run_the_test(self, expected_ride_count, expected_total_cost):
        self.assertEqual(self.user.get_num_rides(), expected_ride_count)
        self.assertEqual(self.user.get_total_spent(), expected_total_cost)

    def set_cost(self, cost):
        self.ride.cost = cost
        self.user.add_completed_ride(self.ride)

