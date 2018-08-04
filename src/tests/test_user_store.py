import unittest
from ..user_store import UserStore

class UserStoreTest(unittest.TestCase):
    def setUp(self):
        self.user_store = UserStore()
        self.user_id = 123
    
    def test_get_user(self):
        """Get user should create user first time it sees ID and return user subsequent times"""
        user = self.user_store.get_user(self.user_id)
        self.assertEqual(user.id, self.user_id)
        self.assertEqual(user.get_total_spent(), 0)
        self.assertEqual(user.get_num_rides(), 0)
        user.total_spent = 14.57
        user.num_rides = 3
        user2 = self.user_store.get_user(self.user_id)
        self.assertEqual(user2.get_total_spent(), 14.57)
        self.assertEqual(user2.get_num_rides(), 3)

    def test_get_user_list(self):
        """Get user list should have a complete list of all users obtained via get_user"""
        i = 0
        while (i<5):
            self.user_store.get_user(self.user_id+i)
            i += 1
        self.assertEqual(len(self.user_store.get_user_list()), 5)
        
