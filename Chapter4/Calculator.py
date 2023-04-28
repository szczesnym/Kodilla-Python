import sys
import logging
from functools import reduce

logging.basicConfig(filename='calculator.log', level=logging.DEBUG)


def action_to_string(action):
    if action == 1:
        return 'Dodawanie'
    if action == 2:
        return 'Odejmowanie'
    if action == 3:
        return 'Mnożenie'
    if action == 4:
        return 'Dzielenie'


def calculate(operator, elements):
    if operator == 1:
        return elements.sum()
    if operator == 3:
        return reduce((lambda x, y: x * y), elements)
    if operator == 2:
        return elements[1] - elements[0]
    if operator == 4:
        if elements[0] == 0:
            return "NO DIVISION by zero"
        else:
            return elements[1] / elements[0]


while True:
    try:
        action = int(input(
            'Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:'))
        break
    except ValueError:
        print('Nie wprowadzono liczby')
logging.debug(f'Key entered {action}')

items = []
if action == 1 or action == 3:
    text_input = ''
    print(f'Podawaj składniki dla operacji {action_to_string(action)}, aby zakończyć wprowadź .')
    while text_input != '.':
        elem = input(f'Składnik {len(items) + 1}:')
        logging.debug(f'Input for {action} entered {elem}')
        try:
            items.append(int(elem))
        except:
            if elem == '.':
                break
            else:
                print('To nie jest liczba - wprowadź liczbę lub .')
else:
    for i in range(1, 3):
        while True:
            elem = input(f'Składnik {len(items) + 1}:')
            logging.debug(f'Input for {action} entered {elem}')
            try:
                items.append(int(elem))
                break
            except:
                print('To nie jest liczba - wprowadź liczbę lub .')

print(calculate(action, items))
