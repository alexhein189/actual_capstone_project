#dictionary, key= name, value = item object,
# stock is most important, updating, whether the item should be added or removed


class item:

    def __init__(self, name:str, barcode:int, price:float, stock_quantity:int, limiting_number:int):
        self.name = name
        self.barcode = barcode
        self.price = price
        self.stock_quantity = stock_quantity
        self.limiting_number = limiting_number