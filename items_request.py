#when vulnerable person request some items
from typing import List

import datetime


class itemsRequest:
    def __init__(self, vulnerable_id_code:str, items:List[str], start_date:datetime.datetime, end_date:datetime.datetime, emergency:int, number_of_shops, main_dictionary):
        self.items = items #string
        self.vulnerable_id_code = vulnerable_id_code
        self.start_date = start_date
        self.end_date = end_date
        self.priority_hours = ((end_date - start_date).total_seconds() // 3600)  #time
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
        pass



# May 22nd (7 days ago) : vulnerable A wants items by june 1st (priority : within 10 days)
# May 29th (today) : vulnerable B wants items by May 31st (priority: within 2 days)





