from Unit import Unit


class Item:
    def __init__(self, name, unit_name, unit_price):
        self.name = name
        self.unit = Unit(unit_name)
        self.unit_price = unit_price
