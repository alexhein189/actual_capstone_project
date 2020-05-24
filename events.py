# event is a linked-list with a start-location(node), end-location(node) and duration (edge)

class event:

    def __init__(self, start_location: (float, float), end_location: (float, float), duration: float):
        self.start_location = start_location
        self.end_location = end_location
        self.duration = duration


