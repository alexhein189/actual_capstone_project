from scheduling2 import available_time
from typing import Dict
from typing import List
from collections import deque

from _grid import grid

#timestamp: Dict[int, List[int]]

class volunteer_var:

    def __init__(self, name: str, username: str, id_code: str,
                 latitude:float, longitude:float, availability: Dict[int, List[(int, int)]], available_range:float, grid_:grid, dictionary):
        self.name = name
        self.username = username
        self.id_code = id_code
        for day in availability:
            availability[day].sort()
        self.availability = availability
        self.schedule = {}
        self.longitude = longitude
        self.latitude = latitude
        self.available_range = available_range
        self.deque_of_vulnerable_people = deque()
        self.dictionary = dictionary
        dictionary[id_code] = self
        self.nearest_shops = {}
        self.nearest_vulnerable_people = {}
        grid_.add_user_(latitude, longitude, id_code)
        for id, distance in grid_.get_nearest_users(latitude, longitude, id_code, dictionary, available_range).items():
            self.add_nearest_user(id, distance)

    def add_nearest_user(self, id, distance):
        if distance <= self.available_range:
            if id.startswith("SH"):
                self.nearest_shops[id] = distance
                for vulner_id in self.nearest_vulnerable_people:
                    # TODO: this is just distance from volunteer to shop
                    self.dictionary[vulner_id].accessible_shops[id] = distance
            if id.startswith("VP"):
                self.nearest_vulnerable_people[id] = distance

    def add_to_deque(self, volunteer_task):
        self.deque_of_vulnerable_people.append(volunteer_task)

    def add_to_schedule(self, day, interval, task):
        amount_of_time = task.calculate_time_take()
        interval_length = interval[1]- interval[0]

        if day not in self.schedule:
            self.schedule[day] = {}
        if interval not in self.schedule[day]:
            self.schedule[day][interval] = {task: amount_of_time, "free": interval_length - amount_of_time}
        else:
            self.schedule[day][interval][task] = task.amount_of_time
            self.schedule[day][interval]["free"] -= task.amount_of_time
