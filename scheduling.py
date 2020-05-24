#how many volunteers can be efficiently allocated to one volunteer
#system-level ds: is a linked-list

class Scheduling:

    def __init__(self, duration, distance, event:List[timestamp], available_time:List[timestamp]):
        self.duration = duration
        self.distance = distance
        self.event = event #linked-list
        self.available_time = available_time

    def add_event(self):
        return

    def remove_event(self):
        return