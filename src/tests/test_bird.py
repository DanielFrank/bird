import unittest
from ..ride import Ride
from ..bird import Bird

class BirdTest(unittest.TestCase):
    def setUp(self):
        self.user_id = 1234
        self.bird_id = "ABCD"
        self.pointA = tuple([19, 21])
        self.bird = Bird(self.bird_id, self.pointA)
    
    def test_initialize(self):
        """A bird should correctly set bird_id"""
        self.assertEqual(self.bird.id, self.bird_id)
        
    def test_check_end_ride(self):
        """ Confirm that ride created by start_ride is manipulated in end_ride"""
        pointB = tuple([16, 17])
        ride = self.bird.start_ride(self.user_id, self.pointA, 0)
        self.bird.end_ride(pointB, 60)
        self.assertEqual(ride.get_distance(), 5)        
        self.assertEqual(ride.get_cost(), 1.15)        
        self.assertEqual(ride.get_time(), 60)        

    def test_get_distance_from_drop_position(self):
        """A bird's distance from drop position should equal the cartesian distance between current and drop position"""
        self.bird.current_position = tuple([-21, 12])
        self.assertEqual(self.bird.get_distance_from_drop_position(), 41)    
        
    def test_total_distance(self):
        """A bird's total distance should equal the distances for all the rides it took"""
        pointB = tuple([31, 26])
        pointC = tuple([40, -14])
        self.assertEqual(self.bird.get_total_distance(), 0)
        self.bird.start_ride(self.user_id, self.pointA, 10)    
        self.bird.end_ride(pointB, 50)        
        self.assertEqual(self.bird.get_total_distance(), 13)        
        self.bird.start_ride(self.user_id, pointB, 100)        
        self.bird.end_ride(pointC, 120)        
        self.assertEqual(self.bird.get_total_distance(), 54)

    def test_longest_distance(self):
        time_value = 250
        self.bird.start_ride(self.user_id, self.pointA, time_value)
        time_value +=50
        self.bird.end_ride(self.pointA, time_value)       
        time_value +=500
        self.bird.start_ride(self.user_id, self.pointA, time_value)
        self.assertEqual(self.bird.get_longest_wait(), 500)
        time_value +=200
        self.bird.end_ride(self.pointA, time_value)       
        time_value +=300
        self.bird.start_ride(self.user_id, self.pointA, time_value)
        self.assertEqual(self.bird.get_longest_wait(), 500)
        time_value +=200
        self.bird.end_ride(self.pointA, time_value)       
        time_value +=700
        self.bird.start_ride(self.user_id, self.pointA, time_value)
        self.assertEqual(self.bird.get_longest_wait(), 700)
