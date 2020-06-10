from items_request import itemsRequest
from user_dataframe import user_df

class vulnerable_person:
    #TODO: put the vulnerable person object directly in the dataframe by implementing that in the constructor
    def __init__(self,name:str, username:str,id_code:int, longitude, latitude, postcode:str):
        self.name = name
        self.public_username = username
        self.private_id_code = id_code
        self.longitude = longitude
        self.latitude = latitude
        self.postcode = postcode

    def request_items(self,list_of_essentials, start_date, priority_hours, emergency_rating):
        return itemsRequest(self,list_of_essentials, start_date, priority_hours, emergency_rating)

    #TODO: change type of listo_of_essentials to type item rather than string.