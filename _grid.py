from typing import Dict

from distance import distance
from math import ceil


class grid:
    def __init__(self):
        self.dictionary_of_places = {}

    def add_user_(self, latitude, longitude, new_user_id):
        x = int(latitude * 10)
        y = int(longitude * 10)
        if (x, y) not in self.dictionary_of_places:
            self.dictionary_of_places[(x, y)] = []
        self.dictionary_of_places[(x, y)].append(new_user_id)

    # def adjacent_generator(self, latitude,longitude):
    #     x = int(latitude * 10)
    #     y = int(longitude * 10)
    #     max_x = int((latitude + 0.1) * 10)
    #     min_x = int((latitude - 0.1) * 10)
    #     max_y = int((longitude + 0.1) * 10)
    #     min_y = int((longitude - 0.1) * 10)
    #     list_of_adjacent_coord = [(max_x, max_y), (min_x,min_y),(min_x, max_y), (max_x,min_y), (x, max_y),(max_x,y), (min_x,y),(x,min_y), (x,y)]
    #     list_of_places = []
    #     for i in range(len(list_of_adjacent_coord)):
    #         list_of_places.append(self.dictionary_of_places[list_of_adjacent_coord[i]])
    #     return list_of_places

    # def get_nearest_users(self, latitude, longitude):
    #     x = int(latitude * 10)
    #     y = int(longitude * 10)
    #     dictionary = user_dictionary({})
    #     for i in [x - 1, x, x + 1]:
    #         for j in [y - 1, y, y + 1]:
    #             for user in self.dictionary_of_places[(i, j)].user_hash.values():
    #                 # TODO: To make sure where the latitude and longitude are coming from
    #                 d = distance(latitude, longitude, user.latitude, user.longitude).calculate_distance()
    #                 if d < 2.5:
    #                     dictionary.add_user(user)
    #     return dictionary

    def get_nearest_users(self, latitude, longitude, new_user_id, dictionary, available_range=20):
        x = int(latitude * 10)
        y = int(longitude * 10)
        distance_dict = {}
        no_squares = ceil(available_range / 5)
        for i in range(x - no_squares, x + no_squares + 1):
            for j in range(y - no_squares, y + no_squares + 1):
                if (i, j) in self.dictionary_of_places:
                    for id in self.dictionary_of_places[(i, j)]:
                        user = dictionary[id]
                        # TODO: To make sure where the latitude and longitude are coming from
                        d = distance(latitude, longitude, user.latitude, user.longitude).calculate_distance()
                        if d < available_range and (d < user.available_range if id.startswith("VO") else True):
                            distance_dict[id] = d
        for id, d in distance_dict.items():
            dictionary[id].add_nearest_user(new_user_id, d)
        return distance_dict
