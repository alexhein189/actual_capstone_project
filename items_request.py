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




# May 22nd (7 days ago) : vulnerable A wants items by june 1st (priority : within 10 days)
# May 29th (today) : vulnerable B wants items by May 31st (priority: within 2 days)





