#when vulnerable person request some items
from typing import List, Dict

import datetime


class itemsRequest:
    def __init__(self, vulnerable_id_code:str, items:List[str], start_date:datetime.datetime, end_date:datetime.datetime, emergency:int, number_of_shops, main_dictionary):
        self.items = items #string
        self.vulnerable_id_code = vulnerable_id_code
        self.start_date = start_date
        self.end_date = end_date
        self.main_dictionary= main_dictionary
        self.priority_hours = int(((end_date - start_date).total_seconds() // 3600))#time
        self.difference_in_days = (self.priority_hours) // 24
        self.nearest_volunteers = main_dictionary[vulnerable_id_code].nearest_volunteers
        self.emergency = emergency
        self.number_of_shops = number_of_shops

    def finding_remaining_hours(self):
        number_of_hours_since_start = ((datetime.datetime.now() - self.start_date).total_seconds() // 3600)
        number_of_hours_left = self.priority_hours - number_of_hours_since_start
        return number_of_hours_left

    def emergency_index_generator(self):
        # TODO: maybe change + of shopkeeper available in range to -
        priority_score = self.finding_remaining_hours() + self.emergency + self.number_of_shops
        return priority_score

    def find_volunteers_with_time(self):
        list_of_ids = []
        for i in range(self.difference_in_days):
            for id in self.nearest_volunteers:
                if (self.start_date.weekday()+i) % 7 in self.main_dictionary[id].timestamp:
                    if id not in list_of_ids:
                        list_of_ids.append(id)
        return list_of_ids

    def finding_shops_with_items(self, list_of_volunteer_ids):
        dictionary_of_shops ={}
        dictionary_of_items = {}
        for id in list_of_volunteer_ids:
            for shop_id in self.main_dictionary[id].nearest_shops:
                list_of_items =[]
                for item in self.items:
                    if item in self.main_dictionary[shop_id].items_in_stock:
                        list_of_items.append(item)
                        if item not in dictionary_of_items:
                            dictionary_of_items[item] = []
                        dictionary_of_items[item].append(shop_id)
                if len(list_of_items) >= 1:
                    dictionary_of_shops[shop_id] = list_of_items
        return dictionary_of_shops, dictionary_of_items

    def finding_optimal_combination(self, dictionary_of_user, dictionary_of_items):
        sorted_user_ids = sorted(list(dictionary_of_user.keys()), key=lambda x: len(dictionary_of_user[x]))
        list_of_optimal_users = []
        for user_id in sorted_user_ids:
            counter = 0
            for item in dictionary_of_user[user_id]:
                if len(dictionary_of_items[item]) > 1:
                    counter +=1
            if counter == len(dictionary_of_user[user_id]):
                del dictionary_of_user[user_id]
            else:
                list_of_optimal_users.append(user_id)
        return list_of_optimal_users

    def finding_dictionary_of_volunteers_with_shops(self, list_of_volunteers, list_of_shops):
        dictionary_of_shop_to_volun = {}
        dictionary_of_volun_to_shop = {}
        for volunteer in list_of_volunteers:
            list_of_shops_for_volunteer = []
            for shop in list_of_shops:
                if shop in self.main_dictionary[volunteer].nearest_shops:
                    list_of_shops_for_volunteer.append(shop)
                    if shop not in dictionary_of_shop_to_volun:
                        dictionary_of_shop_to_volun[shop] = []
                    dictionary_of_shop_to_volun[shop].append(volunteer)
            if len(list_of_shops_for_volunteer) >= 1:
                dictionary_of_volun_to_shop[volunteer] = list_of_shops_for_volunteer

        return dictionary_of_volun_to_shop, dictionary_of_shop_to_volun

    # for _ in dictionary_of_user:
    #     min_number_of_items = len(self.items) + 1
    #     user_id_with_min_number_of_items = None
    #     for user_id in dictionary_of_user:
    #         if user_id in list_of_optimal_users:
    #             continue
    #         number_of_items = len(dictionary_of_user[user_id])
    #         if number_of_items < min_number_of_items:
    #             min_number_of_items = number_of_items
    #             user_id_with_min_number_of_items = user_id

    def finding_best_match_between_shops_and_volunteers(self, list_of_volunteers, list_of_shops):
        dictionary_of_shop_to_volun = {}
        for shop in list_of_shops:
            min_volunteer_distance = 20
            min_volunteer_id = None
            for volunteer in list_of_volunteers:
                if shop in self.main_dictionary[volunteer].nearest_shops:
                    distance = self.main_dictionary[volunteer].nearest_shops[shop]
                    if distance < min_volunteer_distance:
                        min_volunteer_distance = distance
                        min_volunteer_id = volunteer
            dictionary_of_shop_to_volun[shop] = min_volunteer_id

        return dictionary_of_shop_to_volun


    def matching_volunteers_and_shops(self):
        list_of_available_volunteers = self.find_volunteers_with_time()
        dictionary_of_shops_with_items, dictionary_of_items_with_shops = self.finding_shops_with_items(list_of_available_volunteers)

        list_of_optimal_shops = self.finding_optimal_combination(dictionary_of_shops_with_items, dictionary_of_items_with_shops)
        dictionary_of_volun_to_shop, dictionary_of_shop_to_volun = self.finding_dictionary_of_volunteers_with_shops(list_of_available_volunteers,list_of_optimal_shops)
        list_of_optimal_volunteers = self.finding_optimal_combination(dictionary_of_volun_to_shop, dictionary_of_shop_to_volun)
        dictionary_of_shop_to_volun_optimal = self.finding_best_match_between_shops_and_volunteers(list_of_optimal_volunteers, list_of_optimal_shops)

        return dictionary_of_shop_to_volun_optimal






# May 22nd (7 days ago) : vulnerable A wants items by june 1st (priority : within 10 days)
# May 29th (today) : vulnerable B wants items by May 31st (priority: within 2 days)





