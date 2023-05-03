from Warehouse import Warehouse
import sys


def show_help(list_of_args):
    if len(list_of_args) > 0:
        help_key = list_of_args[0].upper()
        if help_key in help.keys():
            print(f'Help on \033[92m{list_of_args[0]}\033[0m\n {help.get(help_key)}')
        else:
            print(f'Cannot find help on \033[91m{help_key}\033[0m')
    else:
        print('List of commands:')
        print('add_item\nshow\nadd\nsell\nshow_revenue\nsave\nload\nexit')
        print('To get more information type \033[92m help <option> \033[0mex.\033[92m help add\033[0m')


help = {'ADD_ITEM': 'Help on add_item command',
        'SHOW': 'Help on show command',
        'SELL': 'Help on sell command',
        'SHOW_REVENUE': 'Help on show revenue command',
        'SAVE': 'Help on save command',
        'LOAD': 'Help on load command',
        'EXIT': 'Exit is exit',
       }

command = ''
print('Type help to get list of options')
while command.upper() != 'EXIT':
    command = input('What would like to do ?:')
    if 'HELP' in command.upper().strip():
        command_params = command.split(' ')
        show_help(command_params[1:])
