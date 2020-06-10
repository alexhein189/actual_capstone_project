from distance import distance

class address_availablity:
    def __init__(self, address:(float, float), range_in_miles:float):
        self.address = address
        self.range_in_miles = range_in_miles


    def calculate_distance(self):
        distance_between_two_points = distance(self.address[0],self.address[1])
