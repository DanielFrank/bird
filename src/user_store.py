#Should probably make this a singleton but not worth the effort

from .user import User

class UserStore:
    
    def __init__(self):
        self.user_dict = dict()
    
    def get_user(self, user_id):
        if (user_id in self.user_dict):
            return self.user_dict[user_id]        
        user = User(user_id)
        self.user_dict[user_id] = user
        return user

    def get_user_list(self):
        return self.user_dict.values()