#!/usr/bin/env python3

from os import path
from src.menu import Menu
import os

def run():
    path_to_settings = os.path.join(os.path.dirname(os.path.abspath(__file__))) + '/settings/settings.json'
    menu = Menu(path_to_settings)

    if not menu.error:
        running = True

    else:
        print('error in settings')
        running = False

    print('Version 0.0.0')    

    while running:
        print('Type "rename", "help", "settings", "quit"')
        user_input = input('>>> ')

        if user_input == 'rename':
            menu.rename()

        elif user_input == 'settings':
            menu.new_settings()

        elif user_input == 'help':
            menu.help()

        elif user_input == 'quit':
            running = False

if __name__ == '__main__':
    run()