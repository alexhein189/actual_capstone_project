from address_availablity import address_availablity
from scheduling import Scheduling

class volunteer:

    def __init__(self, name:str, username:str, id_code:int, schedule:List[Scheduling], available_location:address_availablity):
        self.name = name
        self.public_username = username #string
        self.private_id_code = id_code #int
        self.schedule = schedule
        self.available_location = available_location

