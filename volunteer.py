from address_availablity import address_availablity
from scheduling2 import available_time


class volunteer:

    def __init__(self, name: str, username: str, id_code: int, timestamp: available_time,
                 available_location: address_availablity):
        self.name = name
        self.public_username = username  # string
        self.private_id_code = id_code  # int
        self.timestamp = timestamp
        self.available_location = available_location
