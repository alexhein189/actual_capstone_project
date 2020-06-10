from typing import Dict
from nouserexcept import NoUserException


class user_df:

    def __init__(self, user_hash: Dict):
        self.user_hash = user_hash

    def contains_user(self, user_id):
        if user_id in self.user_hash:
            return True
        return False

    def add_user(self, new_user):
        # TODO: decide on the keys of the Dictionary
        self.user_hash[new_user.id_code] = new_user
        self.user_hash[(new_user.latitude, new_user.longitude)] = new_user

    def remove_user(self, user_id):
        if self.contains_user(user_id):
            del self.user_hash[user_id]
        else:
            raise NoUserException()
