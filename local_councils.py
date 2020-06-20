from vulnerable_person import vulnerable_person

class the_local_council:
    def __init__(self, main_dictionary, grid):
        self.main_dictionary = main_dictionary
        self.grid = grid

    def register_vuln(self, name, username,id_code, latitude, longitude, conditions):
        return vulnerable_person(name, username, id_code, latitude, longitude, conditions, self.grid, self.main_dictionary)

    def delete_vuln(self, id_code):
        del self.main_dictionary[id_code]

    def update_conditions(self, id_code, condition):
        self.main_dictionary[id_code].conditions = condition
