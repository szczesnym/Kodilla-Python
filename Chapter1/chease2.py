from typing import List


class Cheese:
    def __init__(self, name, price, amount=1.0):
        self.name = name
        self.price = price
        self.amount = amount

    def __str__(self):
        priceStr = f'{self.price:#3.2f}'
        amountStr = f'{self.amount:#3.2f}'
        return f'Produkt {self.name} masa {amountStr.replace(".", ",")}kg w cenie {priceStr.replace(".", ",")} PLN/kg'

    def value(self):
        return self.amount * self.price


cheeses: List[Cheese] = [Cheese('roquefort', 12.50, 2), Cheese('stilton', 11.24), Cheese('brie', 9.30),
                         Cheese('gouda', 8.55), Cheese('edam', 11), Cheese('parmezan', 16.50, 3.5),
                         Cheese('mozzarella', 14, 0.13), Cheese('czechosłowacki ser z owczego mleka', 122.32, 0.22)]

total = 0
print('W koszyku znalazło się:')
for cheese in cheeses:
    print(cheese)
    total += cheese.value()
print(f'Suma: {total:#5.2f} PLN')
