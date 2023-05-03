from StoreItem import StoreItem
from Item import Item


class Warehouse:
    def __int__(self):
        self.stock_items = {}
        self.stock_items_count = 0
        self.items_leger = {} # sold_items combined with

    def add_item(self, item, quantity):
        pass

    def remove_quantity(self, item, quantity):
        pass

    def get_stock_value(self):
        pass

    def get_income(self):
        pass

    def get_costs(self):
        pass

    def show_revenue(self):
        pass

    def export_items_to_csv(self):
        pass

    def load_items_from_csv(self):
        pass