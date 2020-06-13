from _grid import grid
from shop_keeper import shop_keeper
from volunteer_2 import volunteer_var
from vulnerable_person import vulnerable_person

import pickle
import os

filename = "grid.pkl"
if os.path.exists(filename):
    with open(filename, "rb") as file:
        main_grid = pickle.load(file)
else:
    main_grid = grid()
print(main_grid.dictionary_of_places)

all_users_filename = "all_users.pkl"
if os.path.exists(all_users_filename):
    with open(all_users_filename, "rb") as file:
        main_users_dictionary = pickle.load(file)
else:
    main_users_dictionary = {}

print(main_users_dictionary)


def asking_vulnerable_person():
    name = input("Name:")
    username = input("Username:")
    user_id_int = int(input("User Id:"))
    user_id = "VP"+str(user_id_int)
    latitude = float(input("Latitude:"))
    longitude = float(input("Longitude:"))
    new_vulnerable_person = vulnerable_person(name, username, user_id, latitude, longitude, main_grid, main_vulnerable_dictionary)



# def asking_volunteer():
#     name = input("Name:")
#     username = input("Username:")
#     user_id = int(input("User Id:"))
#     timestamp = int(input("User Id:"))
#     latitude = float(input("Latitude:"))
#     longitude = float(input("Longitude:"))
#     vulnerable_person(name, username, user_id, latitude, longitude, main_grid)

print('hello_world')

# user_type = int(input("Are you a vulnerable person(1), volunteer (2) or a shopkeeper (3)"))

harris_shop = shop_keeper("Harris Food", "SH84983", 51.2310572,-0.122247, {},main_grid, main_users_dictionary)
tesco_express = shop_keeper("Tesco Express", "SH12937", 51.25234474,-0.1380595, {},main_grid, main_users_dictionary)
sainsbury = shop_keeper("Sainsbury", "SH52341", 51.1275303,-0.1351368, {},main_grid, main_users_dictionary)
john_walker = shop_keeper("John Walker", "SH34522", 51.1268855,-0.1256531, {},main_grid, main_users_dictionary)

volunteer_c = volunteer_var("Tara", "tara101", "VO87326", 51.2275303,-0.1351368, 3,main_grid, main_users_dictionary)
volunteer_d = volunteer_var("John","john101", "VO39285", 51.2268855,-0.1556531, 4.5,main_grid, main_users_dictionary)
volunteer_a = volunteer_var("Albert", "albert101", "VO67564", 51.18412,-0.18234, 4.5,main_grid, main_users_dictionary)
volunteer_e = volunteer_var("Robert","robert101", "VO54761", 51.3268855,-0.2256531, 2,main_grid, main_users_dictionary)
volunteer_f = volunteer_var("Daniel","daniel101", "VO33333", 51.3368855,-0.1396531, 2,main_grid, main_users_dictionary)
volunteer_b = volunteer_var("Jane", "jane101", "VO92345", 51.19528862,-0.16214, 4,main_grid, main_users_dictionary)

mary_vulnerable = vulnerable_person("Mary", "mary101","VP23123", 51.122445, -0.12983, main_grid,main_users_dictionary )
chris_vulnerable = vulnerable_person("Chris", "chris101","VP91234", 51.19123, -0.16854, main_grid,main_users_dictionary)
alice_vulnerable = vulnerable_person("Alice", "alice101","VP78743", 51.24521, -0.14766, main_grid,main_users_dictionary)
kate_vulnerable = vulnerable_person("Kate", "kate101","VP33219", 51.34521, -0.2511, main_grid,main_users_dictionary)

# Harris food (51.2310572,-0.122247)
# Tesco Express(51.25234474,-0.1380595)
# Sainsbury(51.1275303,-0.1351368)
# M&S(51.1269766,-0.1329754)
# John Walker(51.1268855,-0.1256531)


with open(filename, "wb") as file:
    pickle.dump(main_grid, file)

with open(all_users_filename, "wb") as file:
    pickle.dump(main_users_dictionary, file)

# grid_example = grid()


#{(511,-1):[mary, chris],(512,-1):[alice]}