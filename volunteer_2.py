from scheduling2 import available_time
from typing import Dict
from user_dataframe import user_df
from _grid import grid
from user_dataframe import user_df


class volunteer_var:

    def __init__(self, name: str, username: str, id_code: str,
                 latitude:float, longitude:float, available_range:float, grid_:grid, df: user_df):
        self.name = name
        self.username = username
        self.id_code = id_code
        #self.timestamp = timestamp
        self.longitude = longitude
        self.latitude = latitude
        self.available_range = available_range

        df.add_user(self)
        self.nearest_shops = {}
        self.nearest_vulnerable_people = {}
        grid_.add_user_(latitude, longitude, id_code)
        for id, distance in grid_.get_nearest_users(latitude, longitude, id_code, df, available_range).items():
            self.add_nearest_user(id, distance)

    def add_nearest_user(self, id, distance):
        if distance <= self.available_range:
            if id.startswith("SH"):
                self.nearest_shops[id] = distance
            if id.startswith("VP"):
                self.nearest_vulnerable_people[id] = distance