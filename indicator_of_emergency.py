import datetime

from items_request import itemsRequest

from _grid import grid

#TODO: GET RID OF EMERGENCY INDEX ALL TOGETHER
#_____________________________________________

class emergency_index:
    def __init__(self, item_request: itemsRequest, shop_keeper_grid: grid):
        self.item_request = item_request
        self.shopkeeper_grid = shop_keeper_grid

    def finding_remaining_hours(self):
        return -self.item_request.finding_remaining_hours()

    def return_emergency_number(self):
        #TODO: Limit emergency number from between 1 to 10
        return self.item_request.emergency

    def shopkeeper_available_in_range(self, latitude, longitude):
        #TODO: change the sign of the priority value here
        list_of_shops_available = self.shopkeeper_grid.get_nearest_users(latitude, longitude)
        return len(list_of_shops_available)

    def add_up_score(self):
        #TODO: maybe change + of shopkeeper available in range to -
        priority_score = self.finding_remaining_hours() + self.return_emergency_number() + self.shopkeeper_available_in_range()
        return priority_score


