from datetime import datetime

class volunteer_task:
    def __init__(self, item_request_id, vulnerable_id_code, volunteer_id_code, shops_and_items, end_date, main_dictionary):
        self.vulnerable_idcode = vulnerable_id_code
        self.volunteer_id_code = volunteer_id_code
        self.item_request_id = item_request_id
        self.shops_and_items = shops_and_items
        self.start_date = datetime.today()
        self.end_date = end_date
        self.main_dictionary = main_dictionary
        self.time_taken_for_task = 0


    def calculate_time_take(self):
        if len(self.main_dictionary[self.volunteer_id_code].deque_of_vulnerable_people) == 0:
            pass

