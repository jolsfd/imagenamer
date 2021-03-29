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
        path = input('Please input a path: ')
        
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
        print(F'Enter new settings. If you do not want to change press "Enter"')

        # Get new attributes from user
        new_safe_string = input(F'New safe string: ')
        new_space_letter = input(F'New space letter: ')
        add_image_extension = input(F'Add new image extension: ')
        add_raw_extension = input(F'Add new raw extension: ')
        del_image_extension = input(F'Remove image extension:')
        del_raw_extension = input(F'Remove raw extension: ')

        if self.settings['raw_rename'] == False:
            raw_rename_input = input(F'Do you want to enable raw renaming ? [y/n]')

        else:
            raw_rename_input = input(F'Do you want to diable raw renaming ? [y/n]')

        # Make new settings
        new_settings = self.settings

        # Change attributes in new settings
        if raw_rename_input == 'y':

            if self.settings['raw_rename'] == False:
                new_settings['raw_rename'] = True

            else:
                new_settings['raw_rename'] = False

        if len(new_safe_string) > 0:
            new_settings['safe_string'] = new_safe_string

        if len(new_space_letter) > 0:
            new_settings['space_letter'] = new_space_letter

        if len(add_image_extension) > 0:
            new_settings['image_ext'].append(add_image_extension)

        if len(add_raw_extension) > 0:
            new_settings['raw_ext'].append(add_raw_extension)

        if len(del_image_extension) > 0:
            try:
                new_settings['image_ext'].remove(del_image_extension)

            except ValueError:
                pass

        if len(del_raw_extension) > 0:
            try:
                new_settings['raw_ext'].remove(del_raw_extension)
            
            except ValueError:
                pass

        # Print new settings
        print(
            F"Safe String: {new_settings['safe_string']}\n"
            F"Space letter: {new_settings['space_letter']}\n"
            F"Image extensions: {new_settings['image_ext']}\n"
            F"Raw extensions: {new_settings['raw_ext']}\n"
            F"Raw renaming: {new_settings['raw_rename']}\n"
        )

        # Confirm new settings
        confirm = input(F'Do you confirm settings ? [y/n]')

        if confirm == 'y':

            # Save new settings into json file
            self.settings_objects.save_settings(new_settings)
            self.rename_object.update_settings(new_settings)

            print(F'New settings have been saved successfully.')

        else:
            print(F'New settings were not saved.')

    def help(self):
        print(
            F'"rename" - renames all images in a folder structure\n'
            F'"settings" - change settings\n'
            F'"quit" - quits the application\n'
            F'For more Help please visit https://github.com/jolsfd/imagenamer/ \n'
            )
