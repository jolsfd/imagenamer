import os
from src.settings import Settings
from src.rename import Rename
import os

class Menu:
    def __init__(self, path_to_settings):
        self.settings_objects = Settings(path_to_settings)
        self.settings = self.settings_objects.load_settings()
        self.error = self.settings_objects.check_settings(self.settings)
        self.rename_object = Rename(self.settings)

    def rename(self):
        path = input('Please input a path')
        
        if '\\' in path:
            path = path.replace('\\','/')

        if os.path.exists(path):
            number_of_images, number_of_raws = self.rename_object.collect_files(path)

            print(F'Rename {number_of_images} images and {number_of_raws} raws')

            user_input = input('Yes/No [y/n]')

            if user_input == 'y':
                self.rename_object.rename_images()
                self.rename_object.clear()

    def new_settings(self):
        print('Enter new settings. If you do not want to change press "Enter"')
        safe_string_input = input(F'Safe String: ')
        raw_rename_input = input(F'Do you want to enable raw renaming ? [y/n]')

        new_settings = self.settings

        if len(safe_string_input) > 1:
            new_settings['safe_string'] = safe_string_input

        if raw_rename_input == 'y':
            new_settings['raw_renaming'] = True

        elif raw_rename_input != 'y':
            new_settings['raw_renaming'] = False

        self.settings_objects.save_settings(new_settings)
        self.rename_object.update_settings(new_settings)

    def help(self):
        print('Help')