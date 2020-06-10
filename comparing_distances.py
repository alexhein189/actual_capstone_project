from distance import distance
from vulnerable_person import vulnerable_person
from volunteer_2 import new_volunteer


class distance_chooser:
    def __init__(self, vulnerable_longitude: vulnerable_person.longitude,
                 vulnerable_latitude: vulnerable_person.latitude, volunteer_longitude: new_volunteer.longitude,
                 volunteer_latitude: new_volunteer.latitude, volunteer_available_range: new_volunteer.available_range):
        self.vulnerable_longitude = vulnerable_longitude  # (float, float)
        self.vulnerable_latitude = vulnerable_latitude
        self.volunteer_longitude = volunteer_longitude
        self.volunteer_latitude = volunteer_latitude
        self.volunteer_available_range = volunteer_available_range  # int

    def calculate_distance(self):
        distance_between = distance(self.vulnerable_longitude, self.vulnerable_latitude, self.volunteer_longitude,
                                    self.volunteer_latitude)
        return distance_between.calculate_distance()

    def compare_distance(self):
        if self.calculate_distance() <= self.volunteer_available_range:
            return True
        else:
            return False
