#when vulnerable person request some items
from typing import List, Dict
from volunteer_task_file import volunteer_task

import datetime


class itemsRequest:
    def __init__(self, vulnerable_id_code:str, item_request_id:int , items:List[str], start_date:datetime.datetime, end_date:datetime.datetime, emergency:int, number_of_shops, main_dictionary):
        self.items = items #string
        self.item_request_id = item_request_id
        self.vulnerable_id_code = vulnerable_id_code
        self.start_date = start_date
        self.end_date = end_date
        self.main_dictionary= main_dictionary
        self.priority_hours = int(((end_date - start_date).total_seconds() // 3600))#time
        self.difference_in_days = (self.priority_hours) // 24
        # self.difference_in_days_now_and_end = int(((start_date - datetime.datetime.today()).total_seconds() // 3600)) // 24
        self.nearest_volunteers = main_dictionary[vulnerable_id_code].nearest_volunteers
        self.emergency = emergency
        self.number_of_shops = number_of_shops

    def finding_remaining_hours(self):
        number_of_hours_since_start = ((datetime.datetime.now() - self.start_date).total_seconds() // 3600)
        number_of_hours_left = self.priority_hours - number_of_hours_since_start
        return number_of_hours_left

    def emergency_index_generator(self):
        # TODO: maybe change + of shopkeeper available in range to -
        priority_score = 0.5*self.finding_remaining_hours() - 8*self.emergency + 2*self.number_of_shops
        return priority_score

    # TODO: Another conditional that evaluates whether or not there is availability on the day
    # TODO: and in order to do that you have to get the total hours of the time allocated to a volunteer and see
    # TODO: see if that exceeds the hours in the interval, so another method has to be made in the volunteer

    def find_volunteers_with_time(self, dictionary_of_shops):
        now = datetime.datetime.today()
        difference_between_now_and_end_in_days = (self.end_date.date() - now.date()).days
        min_difference_between_now_and_end_in_days = min(difference_between_now_and_end_in_days, 7) #put a comment to explain why you're putting it to 7 which is because volunteers might change next week.
        dictionary_of_volunteer_to_day_to_interval = {}
        for day_after_start_date in range(min_difference_between_now_and_end_in_days): # O(1) because it's 7, it's maximum is 7
            for id in self.nearest_volunteers: #v, v is the number of available volunteers (distance), O(n)
                day = (now.weekday()+day_after_start_date) % 7
                date = now.date() + datetime.timedelta(days=day_after_start_date)
                if day in self.main_dictionary[id].availability:
                    for interval in self.main_dictionary[id].availability[day]: #24 or 13 intervals in one day so it's O(1)
                        if day_after_start_date == 0:
                            # list_of_hours = self.main_dictionary[id].availability[day]
                            if interval[1] <= now.hour:
                                continue
                        elif day_after_start_date == self.difference_in_days - 1:
                            if interval[0] >= self.end_date.hour:
                                break
                        available_shops = {}
                        for shop_id in self.main_dictionary[id].nearest_shops:  # s, where s is the number of shops
                            if shop_id in dictionary_of_shops:
                                available_shops[shop_id] = dictionary_of_shops[shop_id]
                        upperbound_time = volunteer_task(self.item_request_id, self.vulnerable_id_code, id, available_shops, self.end_date, self.main_dictionary).calculate_time_take()

                        if now.hour >= interval[0] and day_after_start_date == 0:

                            if date in self.main_dictionary[id].schedule and interval in self.main_dictionary[id].schedule[date]:
                                if now > self.main_dictionary[id].schedule[date][interval][-1].end_time :
                                    length_of_interval = (datetime.datetime.combine(date, datetime.time(hour=interval[1])) - now).total_seconds() / 60
                                    if upperbound_time < length_of_interval:
                                        dictionary_of_volunteer_to_day_to_interval[id] = (date, interval)
                                        break
                                else:
                                    upperbound_end_time = self.main_dictionary[id].schedule[date][interval][-1].end_time + datetime.timedelta(minutes=upperbound_time)
                                    end_interval_hour = now.replace(hour = interval[1],minute = 0)
                                    if upperbound_end_time < end_interval_hour:
                                        dictionary_of_volunteer_to_day_to_interval[id] = (date, interval)
                                        break
                            # elif now > self.main_dictionary[id].schedule[date][interval][-1].end_time:
                            #     length_of_interval = interval[1] - now
                            #     if upperbound_time < length_of_interval:
                            #         dictionary_of_volunteer_to_day_to_interval[id] = (date, interval)
                            #         break
                            else:
                                length_of_interval = (interval[1]-interval[0]) * 60
                                if upperbound_time < length_of_interval:
                                    dictionary_of_volunteer_to_day_to_interval[id] = (date, interval)
                                    break
                        else:
                            if date not in self.main_dictionary[id].schedule or interval not in self.main_dictionary[id].schedule[date]:
                                length_of_interval = (interval[1] - interval[0]) * 60
                                if upperbound_time < length_of_interval:
                                    dictionary_of_volunteer_to_day_to_interval[id] = (date, interval)
                                    break
                            else:
                                upperbound_end_time = self.main_dictionary[id].schedule[date][interval][
                                                          -1].end_time + datetime.timedelta(minutes=upperbound_time)
                                end_interval_hour = now.replace(hour=interval[1], minute=0)
                                if upperbound_end_time < end_interval_hour:
                                    dictionary_of_volunteer_to_day_to_interval[id] = (date, interval)
                                    break
        #7 x n x 24 = 168n
        #O(vs)
        #TODO: put a maximum on the number of volunteers to consider
        return dictionary_of_volunteer_to_day_to_interval

    def finding_shops_with_items(self):
        dictionary_of_shops ={}
        for shop_id in self.main_dictionary[self.vulnerable_id_code].accessible_shops: #s, where s is the number of shops
            list_of_items =[]
            for item in self.items:#i, where i is the number of items
                if item in self.main_dictionary[shop_id].items_in_stock and self.main_dictionary[shop_id].items_in_stock[item].stock_quantity > 0:
                    list_of_items.append(item)
            if len(list_of_items) >= 1:
                dictionary_of_shops[shop_id] = list_of_items
        #complexity of this algorithm is quadratic O(n^2)
        # O(si)
        #Not for all the cases, so it only does the three loops for unique shops and therefore it is O(si) but the
        #the case that it doesn't, it's just two loops

        return dictionary_of_shops

    def finding_accessible_shops_with_items(self, dictionary_of_shops, list_of_volunteer_ids):
        dictionary_of_items_with_shop_counts = {}
        available_shops = set()
        for id in list_of_volunteer_ids:  # v, where n is the number of volunteers
            for shop_id in self.main_dictionary[id].nearest_shops:  # s, where s is the number of shops
                available_shops.add(shop_id)
        for shop_id in list(dictionary_of_shops.keys()):  # s, where s is the number of shops
            if shop_id not in available_shops:
                del dictionary_of_shops[shop_id]
            else:
                for item in dictionary_of_shops[shop_id]:
                    if item not in dictionary_of_items_with_shop_counts:
                        dictionary_of_items_with_shop_counts[item] = 1
                    else:
                        dictionary_of_items_with_shop_counts[item] += 1

        # complexity of this algorithm is quadratic O(n^2)
        # O(si) + O(vs)
        # Not for all the cases, so it only does the three loops for unique shops and therefore it is O(si) but the
        # the case that it doesn't, it's just two loops

        return dictionary_of_shops, dictionary_of_items_with_shop_counts

    def finding_optimal_combination(self, dictionary_of_user, dictionary_of_items_with_user_counts):
        sorted_user_ids = sorted(list(dictionary_of_user.keys()), key=lambda x: len(dictionary_of_user[x]))#O(n log n), merge sort
        list_of_optimal_users = []
        for user_id in sorted_user_ids: #u, users
            counter = 0
            for item in dictionary_of_user[user_id]: # i, items
                if (dictionary_of_items_with_user_counts[item]) > 1:
                    counter +=1
            if counter == len(dictionary_of_user[user_id]):
                for item in dictionary_of_user[user_id]: #i, times
                    dictionary_of_items_with_user_counts[item] -= 1
                del dictionary_of_user[user_id]
            else:
                list_of_optimal_users.append(user_id)
        # T(n) = u(i) + nlog n; O(n^2)
        return list_of_optimal_users

    def finding_dictionary_of_volunteers_with_shops(self, list_of_volunteers, list_of_shops):
        dictionary_of_shop_to_volun_with_count = {}
        dictionary_of_volun_to_shop = {}
        for volunteer in list_of_volunteers: #v, volunteers O(n)
            if volunteer in dictionary_of_volun_to_shop:
                continue
            list_of_shops_for_volunteer = []
            for shop in list_of_shops: #s, shopkeepers O(n)
                if shop in self.main_dictionary[volunteer].nearest_shops:
                    list_of_shops_for_volunteer.append(shop)
                    if shop not in dictionary_of_shop_to_volun_with_count:
                        dictionary_of_shop_to_volun_with_count[shop] = 1
                    else:
                        dictionary_of_shop_to_volun_with_count[shop] += 1
            if len(list_of_shops_for_volunteer) >= 1:
                dictionary_of_volun_to_shop[volunteer] = list_of_shops_for_volunteer
        #O(sv) => O(n^2)
        return dictionary_of_volun_to_shop, dictionary_of_shop_to_volun_with_count

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
        #complexity is O(n^2):
        # O(sv)
        return dictionary_of_shop_to_volun


    def finding_best_match_between_shops_and_items(self, list_of_items, list_of_shops):
        dictionary_of_item_to_shop = {}
        for item in list_of_items:
            max_quantity_of_item = 0
            max_quantity_shop_id = None
            for shop_id in list_of_shops:
                if item in self.main_dictionary[shop_id].items_in_stock:
                    quantity_of_item = self.main_dictionary[shop_id].items_in_stock[item].stock_quantity
                    if quantity_of_item > max_quantity_of_item:
                        max_quantity_of_item = quantity_of_item
                        max_quantity_shop_id = shop_id
            dictionary_of_item_to_shop[item] = max_quantity_shop_id
        # complexity is O(n^2):
        # O(si)
        return dictionary_of_item_to_shop

    def finding_best_match_vol_shop_item(self, dictionary_of_shop_to_volun_optimal, dictionary_of_item_to_shop_optimal):
        dictionary_of_shop_to_item_optimal = {}
        dictionary_of_vol_to_shop_to_item_optimal = {}
        for item in dictionary_of_item_to_shop_optimal: #i, number of items
            shop = dictionary_of_item_to_shop_optimal[item]
            if shop not in dictionary_of_shop_to_item_optimal:
                dictionary_of_shop_to_item_optimal[shop] = [item]
            else:
                dictionary_of_shop_to_item_optimal[shop].append(item)

        for shop in dictionary_of_shop_to_volun_optimal: #s, number of shops
            volunteer = dictionary_of_shop_to_volun_optimal[shop]
            if volunteer not in dictionary_of_vol_to_shop_to_item_optimal:
                dictionary_of_vol_to_shop_to_item_optimal[volunteer] = {shop:dictionary_of_shop_to_item_optimal[shop]}
            else:
                dictionary_of_vol_to_shop_to_item_optimal[volunteer][shop]= dictionary_of_shop_to_item_optimal[shop]

        # for volunteer in dictionary_of_vol_to_shop_optimal:
        #     dictionary_of_shops_to_specific_volunteer = {}
        #     shops = dictionary_of_vol_to_shop_optimal[volunteer]
        #     for shop_id in shops:
        #         dictionary_of_shops_to_specific_volunteer[shop_id] = dictionary_of_shop_to_item_optimal[shop_id]
        #     dictionary_of_vol_to_shop_item_optimal[volunteer] = dictionary_of_shops_to_specific_volunteer
        # T(n) = n + m  => O(n)
        return dictionary_of_vol_to_shop_to_item_optimal

    def matching_volunteers_and_shops(self):
        dictionary_of_shops_with_items = self.finding_shops_with_items()
        dictionary_of_available_volunteers_with_day_and_interval = self.find_volunteers_with_time(dictionary_of_shops_with_items) # T(n) = 168n,  O(v)
        dictionary_of_shops_with_items, dictionary_of_items_with_shops = self.finding_accessible_shops_with_items(dictionary_of_shops_with_items,dictionary_of_available_volunteers_with_day_and_interval)

        # complexity of this algorithm is O(n^2)
        # O(si) + O(vs)

        list_of_optimal_shops = self.finding_optimal_combination(dictionary_of_shops_with_items, dictionary_of_items_with_shops) # T = s*(i) + nlog n; O(si)
        dictionary_of_item_to_shop_optimal = self.finding_best_match_between_shops_and_items(dictionary_of_items_with_shops.keys(),list_of_optimal_shops) #complexity is O(n^2): O(sv)
        dictionary_of_volun_to_shop, dictionary_of_shop_to_volun = self.finding_dictionary_of_volunteers_with_shops(dictionary_of_available_volunteers_with_day_and_interval,list_of_optimal_shops) # O(si) + O(vs) => O(n^2) quadradic
        list_of_optimal_volunteers = self.finding_optimal_combination(dictionary_of_volun_to_shop, dictionary_of_shop_to_volun) # T= v*(s) + nlog n; O(sv)
        dictionary_of_shop_to_volun_optimal = self.finding_best_match_between_shops_and_volunteers(list_of_optimal_volunteers, list_of_optimal_shops) #complexity is O(n^2): O(sv)

        best_match_vol_shop_item = self.finding_best_match_vol_shop_item(dictionary_of_shop_to_volun_optimal, dictionary_of_item_to_shop_optimal) # T = i + s  => O(s+i)

        for volunteer in best_match_vol_shop_item: #n, number of volunteers
            volunteer_task_specific = volunteer_task(self.item_request_id, self.vulnerable_id_code, volunteer, best_match_vol_shop_item[volunteer], self.end_date, self.main_dictionary)
            day, interval = dictionary_of_available_volunteers_with_day_and_interval[volunteer]
            self.main_dictionary[volunteer].add_to_schedule(day, interval, volunteer_task_specific)
            volunteer_task_specific.reserve_items()

            #O(v) + O(si) + O(vs) +  O(s+i)
            # O(si) + O(vs) => quadratic
            # the more we minimise the shops because the smaller the s the the smaller the overall complexity.
        return best_match_vol_shop_item




# May 22nd (7 days ago) : vulnerable A wants items by june 1st (priority : within 10 days)
# May 29th (today) : vulnerable B wants items by May 31st (priority: within 2 days)





