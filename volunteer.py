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


# avaiable_time_a = ["Tuesdays", "Thursdays"], ["08:00-09:00","09:00-10:00","10:00-11:00","11:00-12:00","12:00-1:00"]
available_time_of_vol_a = available_time(
    {"Tuesdays": ["08:00-09:00", "09:00-10:00", "10:00-11:00"], "Thursdays": ["11:00-12:00", "12:00-1:00"]})
available_location_of_vol_a = address_availablity((213.23, 12.112), 5)
volunteer_A = volunteer("Alex", "getitboy12", 1231, available_time_of_vol_a, available_location_of_vol_a)
print("hello")
