#when vulnerable person request some items
from typing import List
from vulnerable_person import vulnerable_person
import datetime
from indicator_of_emergency import emergency_index


class itemsRequest:
    def __init__(self, the_vulnerable_person:vulnerable_person, items:List[str], start_date:datetime.datetime, priority_hours:int, emergency:int):
        self.items = items #string
        self.the_vulnerable_person = the_vulnerable_person
        self.start_date = start_date
        self.priority_hours = priority_hours  #time
        self.emergency = emergency

    def finding_remaining_hours(self):
        number_of_hours_since_start = ((datetime.datetime.now() - self.start_date).total_seconds() // 3600)
        number_of_hours_left = self.priority_hours - number_of_hours_since_start
        return number_of_hours_left

    def emergency_index_generator(self, grid):
        return emergency_index(self,grid)



# May 22nd (7 days ago) : vulnerable A wants items by june 1st (priority : within 10 days)
# May 29th (today) : vulnerable B wants items by May 31st (priority: within 2 days)





