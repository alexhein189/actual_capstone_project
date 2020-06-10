from scheduling2 import available_time


class volunteer_var:

    def __init__(self, name: str, username: str, id_code: int, timestamp: available_time,
                 longitude:float, latitude:float, available_range:float, post_code:str):
        self.name = name
        self.username = username
        self.id_code = id_code
        self.timestamp = timestamp
        self.longitude = longitude
        self.latitude = latitude
        self.available_range = available_range
        self.post_code = post_code