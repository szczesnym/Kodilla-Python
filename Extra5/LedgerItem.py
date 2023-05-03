from Item import Item


class StoreItem:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

    def get_value(self):
        return self.item.unit_price * self.quantity
