from items_request import itemsRequest
from user_dataframe import user_df
from _grid import grid

class vulnerable_person:
    #TODO: put the vulnerable person object directly in the dataframe by implementing that in the constructor
    def __init__(self,name:str, username:str,id_code:str, latitude, longitude, grid_:grid, df: user_df):
        self.name = name
        self.public_username = username
        self.id_code = id_code
        self.longitude = longitude
        self.latitude = latitude
        df.add_user(self)
        self.nearest_shops = {}
        self.nearest_volunteers = {}
        grid_.add_user_(latitude, longitude, id_code)
        for id, distance in grid_.get_nearest_users(latitude, longitude, id_code, df).items():
            self.add_nearest_user(id, distance)


    def request_items(self,list_of_essentials, start_date, priority_hours, emergency_rating):
        return itemsRequest(self.id_code,list_of_essentials, start_date, priority_hours, emergency_rating, len(self.nearest_shops))

    def add_nearest_user(self, id, distance):
        if id.startswith("SH"):
            self.nearest_shops[id] = distance
        if id.startswith("VO"):
            self.nearest_volunteers[id] = distance






    #TODO: change type of listo_of_essentials to type item rather than string.