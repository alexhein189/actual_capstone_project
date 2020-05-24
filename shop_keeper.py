from items import item
from noitemxexception import NoItemsException


class shop_keeper:

    def __init__(self, shop_name, location, items_in_stock: dict[item]):
        self.shop_name = shop_name
        self.location = location
        self.items_in_stock = items_in_stock

    def contains_item(self, item_name):
        if item_name in self.items_in_stock and (self.items_in_stock[item_name].stock_quantity != 0):
            return True
        return False

    def adds_brand_item(self, item_name, item_barcode, price, stock_quantity, limiting_number):
        new_item = item(item_name, item_barcode, price, stock_quantity, limiting_number)
        self.items_in_stock[item_name] = new_item

    def remove_brand_item(self, item_name):
        if self.contains_item(item_name):
            del self.items_in_stock[item_name]
        else:
            raise NoItemsException()

    def add_stock(self, item_name, additional_quantity):
        self.items_in_stock[item_name].stock_quantity += additional_quantity

    # putting the limit on the number of items
    def remove_stock(self, item_name, removing_quantity):
        if (self.items_in_stock[item_name].stock_quantity >= removing_quantity) and (
                removing_quantity <= self.items_in_stock[item_name].limiting_quantity):
            self.items_in_stock[item_name].stock_quantity -= removing_quantity
        else:
            raise NoItemsException()

    def update_stock_price(self,item_name, new_item_price):
        if self.contains_item(self.items_in_stock[item_name]):
            self.items_in_stock[item_name].price = new_item_price
        else:
            raise NoItemsException()

