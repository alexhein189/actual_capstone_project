#dictionary, key= name, value = item object,
# stock is most important, updating, whether the item should be added or removed

import datetime

class item:

    def __init__(self, name:str, barcode:int, price:float, stock_quantity:int, limiting_number:int, expiration_date:datetime.datetime):
        self.name = name
        self.barcode = barcode
        self.price = price
        self.stock_quantity = stock_quantity
        self.limiting_number = limiting_number
        self.expiration_date = expiration_date