from datetime import datetime
from distance import distance
import random

class volunteer_task:
    def __init__(self, item_request_id, vulnerable_id_code, volunteer_id_code, shops_and_items, end_date, main_dictionary):
        self.vulnerable_idcode = vulnerable_id_code
        self.volunteer_id_code = volunteer_id_code
        self.item_request_id = item_request_id
        self.shops_and_items = shops_and_items
        self.start_date = datetime.today()
        self.end_date = end_date
        self.main_dictionary = main_dictionary
        self.duration = self.calculate_time_take()


    def calculate_time_take(self):
        current_longitude = self.main_dictionary[self.volunteer_id_code].longitude
        current_latitude = self.main_dictionary[self.volunteer_id_code].latitude

        # distance_between_home_and_s1 = distance(volunteer_latitude,random_shop_latitude,volunteer_longitude,random_shop_longitude)
        total_distance_of_locations = 0
        locations = list(self.shops_and_items.keys()) + [self.vulnerable_idcode, self.volunteer_id_code]
        for location_id in locations:
            next_latitude = self.main_dictionary[location_id].latitude
            next_longitude = self.main_dictionary[location_id].longitude
            distance_between_current_location_and_next_shop = distance(current_latitude, current_longitude, next_latitude,
                                                    next_longitude).calculate_distance()
            total_distance_of_locations += distance_between_current_location_and_next_shop
            current_longitude = next_longitude
            current_latitude = next_latitude

        total_time_in_hr = (total_distance_of_locations / 30) #30 mi/hr DRIVING speed
        total_time = total_time_in_hr * 60
        return total_time

    def reserve_items(self):
        for shop in self.shops_and_items:
            self.main_dictionary[shop].reserving_items_for_vul(self.shops_and_items[shop])

