import datetime

from _grid import grid
from shop_keeper import shop_keeper
from volunteer_2 import volunteer_var
from vulnerable_person import vulnerable_person
from all_pending_requests import pending_requests
from items import item

import pickle
import os

filename = "grid2.pkl"
if os.path.exists(filename):
    with open(filename, "rb") as file:
        main_grid = pickle.load(file)
else:
    main_grid = grid()
print(main_grid.dictionary_of_places)

all_users_filename = "all_users2.pkl"
if os.path.exists(all_users_filename):
    with open(all_users_filename, "rb") as file:
        main_users_dictionary = pickle.load(file)
else:
    main_users_dictionary = {}

print(main_users_dictionary)

priority_queue_filename = "priority_queue1.pkl"
if os.path.exists(priority_queue_filename):
    with open(priority_queue_filename, "rb") as file:
        priority_queue = pickle.load(file)
else:
    priority_queue = pending_requests(main_grid)


def asking_vulnerable_person():
    name = input("Name:")
    username = input("Username:")
    user_id_int = int(input("User Id:"))
    user_id = "VP"+str(user_id_int)
    latitude = float(input("Latitude:"))
    longitude = float(input("Longitude:"))
    new_vulnerable_person = vulnerable_person(name, username, user_id, latitude, longitude, main_grid, main_users_dictionary)



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
from unittest.mock import MagicMock
item = MagicMock(stock_quantity=10)
other_item = MagicMock(stock_quantity=10)
item_2 = MagicMock(stock_quantity=5)
item_3 = MagicMock(stock_quantity=3)
item_4 = MagicMock(stock_quantity=6)
harris_shop = shop_keeper("Harris Food", "SH84983", 51.2310572,-0.122247, {"bread":item_3, "biscuits":item_2, "pasta":item_4},main_grid, main_users_dictionary)
tesco_express = shop_keeper("Tesco Express", "SH12937", 51.25234474,-0.1380595, {"rice":item_2,"bread":item_2, "pasta":item_3,"carrots":item_2,"broccoli":item_2, "paracetemol":item_2, "tomatoes":item},main_grid, main_users_dictionary)
sainsbury = shop_keeper("Sainsbury", "SH52341", 51.1275303,-0.1351368, {"rice":item_4,"carrots":item_3,"tomatoes":item_3, "peas":item},main_grid, main_users_dictionary)
john_walker = shop_keeper("John Walker", "SH34522", 51.3491122,-0.2356431, {"paracetemol":item, "cough drops":other_item, "Advil":item_3, "vitamin":item_3},main_grid, main_users_dictionary)
hoodle_shop = shop_keeper("Hoodle Groceries", "SH23943", 51.1410572,-0.125447, {"bread":item_4, "biscuits":item_3, "pasta":item_2, "cough drops":item_2},main_grid, main_users_dictionary)

volunteer_c = volunteer_var("Tara", "tara101", "VO87326", 51.1275303,-0.1351368,{5:[(10, 12), (14,16)],6:[(10, 12), (14,16)],1:[(10, 12), (14,16)]}, 3,main_grid, main_users_dictionary)
volunteer_d = volunteer_var("John","john101", "VO39285", 51.2268855,-0.1556531,{0:[(10, 12), (14,16)],2:[(10, 12), (14,16)],3:[(10, 12), (14,16)], 4:[(10, 12), (14,16)]}, 4.5,main_grid, main_users_dictionary)
volunteer_a = volunteer_var("Albert", "albert101", "VO67564", 51.18412,-0.18234,{3:[(10, 12), (14,16)]}, 4.5,main_grid, main_users_dictionary)
volunteer_e = volunteer_var("Robert","robert101", "VO54761", 51.3268855,-0.2256531,{6:[(10, 12), (14,16)],4:[(10, 12), (14,18)]}, 10,main_grid, main_users_dictionary)
volunteer_f = volunteer_var("Daniel","daniel101", "VO33333", 51.1368855,-0.1396531,{4:[(10, 12), (14,16)],5:[(10, 12), (14,16)],2:[(10, 12), (14,16)]}, 2,main_grid, main_users_dictionary)
volunteer_b = volunteer_var("Jane", "jane101", "VO92345", 51.19528862,-0.16214,{2:[(10, 12), (14,16)],3:[(10, 12), (14,16)]}, 4,main_grid, main_users_dictionary)
volunteer_g = volunteer_var("Gerry", "gerry101", "VO98996", 51.309123,-0.249123,{3:[(10, 12), (14,16)]}, 4,main_grid, main_users_dictionary)

mary_vulnerable = vulnerable_person("Mary", "mary101","VP23123", 51.122445, -0.12983, main_grid,main_users_dictionary )
chris_vulnerable = vulnerable_person("Chris", "chris101","VP91234", 51.19123, -0.16854, main_grid,main_users_dictionary)
alice_vulnerable = vulnerable_person("Alice", "alice101","VP78743", 51.24521, -0.14766, main_grid,main_users_dictionary)
kate_vulnerable = vulnerable_person("Kate", "kate101","VP33219", 51.34521, -0.2511, main_grid,main_users_dictionary)
today = datetime.datetime.today()
test_start_date = today
test_start_date_1 = today - datetime.timedelta(days=2)

mary_vulnerable.request_items("RQ23123",["bread","paracetemol","rice"], today, today+datetime.timedelta(days=1), 1, priority_queue)
chris_vulnerable.request_items("RQ91234",["carrots","paracetemol","rice", "cough drops"], today, today+datetime.timedelta(days=2), 1, priority_queue)
alice_vulnerable.request_items("RQ78743",["biscuits","tomatoes","rice", "paracetemol", "bread"], test_start_date, today+datetime.timedelta(days=1), 1, priority_queue)
kate_vulnerable.request_items("RQ33219",["pasta","tomatoes","cough drops", "paracetemol", "bread"], test_start_date_1, today+datetime.timedelta(days=2), 8, priority_queue)

request_1 =priority_queue.remove_request()
allocation_1 = {main_users_dictionary[request_1.vulnerable_id_code].name:request_1.matching_volunteers_and_shops()}

request_2 =priority_queue.remove_request()
allocation_2 = {main_users_dictionary[request_2.vulnerable_id_code].name:request_2.matching_volunteers_and_shops()}

request_3 =priority_queue.remove_request()
allocation_3 = {main_users_dictionary[request_3.vulnerable_id_code].name:request_3.matching_volunteers_and_shops()}

request_4 =priority_queue.remove_request()
allocation_4 = {main_users_dictionary[request_4.vulnerable_id_code].name:request_4.matching_volunteers_and_shops()}






print('done')
# Harris food (51.2310572,-0.122247)
# Tesco Express(51.25234474,-0.1380595)
# Sainsbury(51.1275303,-0.1351368)
# M&S(51.1269766,-0.1329754)
# John Walker(51.1268855,-0.1256531)


with open(filename, "wb") as file:
    pickle.dump(main_grid, file)

with open(all_users_filename, "wb") as file:
    pickle.dump(main_users_dictionary, file)

with open(priority_queue_filename, "wb") as file:
    pickle.dump(priority_queue, file)

# grid_example = grid()


#{(511,-1):[mary, chris],(512,-1):[alice]}