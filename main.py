#!/usr/bin/env python3

from os import path
from src.menu import Menu
import os
from colorama import Fore, Back, Style


def run():
    path_to_settings = (
        os.path.join(os.path.dirname(os.path.abspath(__file__)))
        + "/settings/settings.json"
    )
    menu = Menu(path_to_settings)

    if not menu.error:
        running = True

    else:
        running = False

    while running:
        print(
            f"Type "
            + Fore.BLUE
            + f"rename"
            + Fore.RESET
            + ", "
            + Fore.BLUE
            + f"help"
            + Fore.RESET
            + ", "
            + Fore.BLUE
            + f"settings"
            + Fore.RESET
            + ", "
            + Fore.BLUE
            + f"quit"
            + Fore.RESET
        )
        user_input = input(">>> ")

        if user_input == "rename":
            menu.rename()

        elif user_input == "settings":
            menu.new_settings()

        elif user_input == "help":
            menu.help()

        elif user_input == "quit":
            running = False


if __name__ == "__main__":
    run()