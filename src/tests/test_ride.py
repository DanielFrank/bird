import unittest
from ..ride import Ride

class RideTest(unittest.TestCase):
    def setUp(self):
        self.user_id = 1234
        self.bird_id = "ABCD"
        self.ride = Ride(self.bird_id, self.user_id)
    
    def test_initialize(self):
        """A ride should correctly set user_id and bird_id"""
        self.assertEqual(self.ride.bird_id, self.bird_id)
        self.assertEqual(self.ride.user_id, self.user_id)
        
    def test_distance(self):
        """A ride's should equal the Cartesian distance between its start and stop points"""
        self.ride.start_ride(tuple([15, 18]), 20)
        self.ride.end_ride(tuple([19, 21]), 120)
        self.assertEqual(self.ride.get_distance(), 5)

    def test_cost_under_a_minute(self):    
        """A ride under a minute should be free"""
        start_time = 50
        self.ride.start_ride(tuple([15, 18]), start_time)
        self.ride.end_ride(tuple([15, 31]), start_time + 52)
        self.assertEqual(self.ride.get_cost(), 0)
    
    def test_cost_time_evenly_divided_by_60(self):    
        """A ride should be $1 to start and .15 per minute"""
        start_time = 100
        self.ride.start_ride(tuple([15, 18]), start_time)
        self.ride.end_ride(tuple([15, 31]), start_time + 120)
        self.assertEqual(self.ride.get_cost(), 1.30)
    
    def test_cost_time_not_evenly_divided_by_60(self):    
        """A ride should be $1 to start and .15 per minute
        If there are extra seconds that should be counted as an additional minute
        """
        start_time = 200
        self.ride.start_ride(tuple([15, 18]), start_time)
        self.ride.end_ride(tuple([15, 31]), start_time + 153)
        self.assertEqual(self.ride.get_cost(), 1.45)
