from scheduling2 import available_time
from typing import Dict
from typing import List
from collections import deque
import datetime

from _grid import grid

#timestamp: Dict[int, List[int]]

class volunteer_var:

    def __init__(self, name: str, username: str, id_code: str,
                 latitude:float, longitude:float, availability, available_range:float, grid_:grid, dictionary:Dict):
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

    def add_to_schedule(self, date, interval, task):
        amount_of_time = task.duration
        if date not in self.schedule:
            self.schedule[date] = {}
        processed_time = datetime.datetime.today()
        start_of_the_interval  = datetime.datetime.combine(date,datetime.time(hour=interval[0]))

        if processed_time < start_of_the_interval:
            if interval not in self.schedule[date]:
                task_deque = deque()

                task.start_time = start_of_the_interval
                task.end_time = start_of_the_interval + datetime.timedelta(minutes=amount_of_time)
                task_deque.append(task)
                self.schedule[date][interval] = task_deque
            else:
                task.start_time = self.schedule[date][interval][-1].end_time
                task.end_time = task.start_time + datetime.timedelta(minutes=amount_of_time)
                self.schedule[date][interval].append(task)
        else:
            if interval not in self.schedule[date]:
                task_deque = deque()
                task.start_time = processed_time
                task.end_time = task.start_time + datetime.timedelta(minutes=amount_of_time)
                task_deque.append(task)
                self.schedule[date][interval] = task_deque
            elif processed_time > self.schedule[date][interval][-1].end_time:
                task.start_time = processed_time
                task.end_time = task.start_time + datetime.timedelta(minutes=amount_of_time)
                self.schedule[date][interval].append(task)
            else:
                task.start_time = self.schedule[date][interval][-1].end_time
                task.end_time = task.start_time + datetime.timedelta(minutes=amount_of_time)
                self.schedule[date][interval].append(task)

        # interval_length = interval[1]- interval[0]
        # if interval not in self.schedule[date]:
        #     self.schedule[date][interval] = {task: amount_of_time, "free": interval_length - amount_of_time}
        # else:
        #     self.schedule[date][interval][task] = amount_of_time
        #     self.schedule[date][interval]["free"] -= amount_of_time
