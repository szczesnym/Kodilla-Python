from Warehouse import Warehouse
import sys


def show_help():
    print('List of commands:')
    print('add_item\nshow\nadd\nsell\nshow_revenue\nsave\nload\nexit')


command = ''

while command.upper() != 'EXIT':
    print('Type help to get list of options')
    command = input('What would like to do ?:')
    if 'HELP' in command.upper().strip():
        show_help()
