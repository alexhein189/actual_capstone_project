import math


class distance:
    def __init__(self, latitude1, longitude1, latitude2, longitude2):
        self.latitude1 = latitude1
        self.longitude1 = longitude1
        self.latitude2 = latitude2
        self.longitude2 = longitude2

    # TODO: Inside the distance, you need to update it, calculate distances in MILES, convert
    def calculate_distance(self):
        return math.sqrt((((self.latitude2 - self.latitude1) * 66.6) ** 2) + (((self.longitude2 - self.longitude1) * 52.6) ** 2))


# distance_between_a_and_b = distance(10, 10, 12, 12)
#
# print(distance_between_a_and_b.calculate_distance())
