import os
from src.settings import Settings
from src.rename import Rename
from colorama import Fore, Back, Style


class Menu:
    def __init__(self, path_to_settings):
        self.settings_objects = Settings(path_to_settings)
        self.settings = self.settings_objects.load_settings()
        self.error = self.settings_objects.check_settings(self.settings)
        self.rename_object = Rename(self.settings)

    def rename(self):
        path = input("Please input a path: ")

        if "\\" in path:
            path = path.replace("\\", "/")

        if os.path.exists(path):
            number_of_images, number_of_raws = self.rename_object.collect_files(path)

            print(f"Rename {number_of_images} images and {number_of_raws} raws")

            user_input = input("Yes/No [y/n]")

            if user_input == "y":
                self.rename_object.rename_images()

        else:
            print(Fore.RED + f"{path} does not exist!" + Fore.RESET)

        self.rename_object.clear()

    def new_settings(self):
        print(f'Enter new settings. If you do not want to change press "Enter"')

        # Get new attributes from user
        new_safe_string = input(f"New safe string: ")
        new_space_letter = input(f"New space letter: ")
        print(Fore.CYAN + f"All Extensions with dot!" + Fore.RESET)
        add_image_extension = input(f"Add new image extension: ")
        add_raw_extension = input(f"Add new raw extension: ")
        del_image_extension = input(f"Remove image extension:")
        del_raw_extension = input(f"Remove raw extension: ")

        if self.settings["raw_rename"] == False:
            raw_rename_input = input(f"Do you want to enable Raw Rename ? [y/n]")

        else:
            raw_rename_input = input(f"Do you want to disable Raw Rename ? [y/n]")

        if self.settings["safe_rename"] == False:
            safe_rename_input = input(f"Do you want to enable Safe Rename ? [y/n]")

        else:
            safe_rename_input = input(f"Do you want to disable Safe Rename ? [y/n]")

        # Make new settings
        new_settings = self.settings

        # Change attributes in new settings
        if raw_rename_input == "y":

            if self.settings["raw_rename"] == False:
                new_settings["raw_rename"] = True

            else:
                new_settings["raw_rename"] = False

        if safe_rename_input == "y":

            if self.settings["safe_rename"] == False:
                new_settings["safe_rename"] = True

            else:
                new_settings["safe_rename"] = False

        if len(new_safe_string) > 0:
            new_settings["safe_string"] = new_safe_string

        if len(new_space_letter) > 0:
            new_settings["space_letter"] = new_space_letter

        if len(add_image_extension) > 0:
            new_settings["image_ext"].append(add_image_extension)

        if len(add_raw_extension) > 0:
            new_settings["raw_ext"].append(add_raw_extension)

        if len(del_image_extension) > 0:
            try:
                new_settings["image_ext"].remove(del_image_extension)

            except ValueError:
                pass

        if len(del_raw_extension) > 0:
            try:
                new_settings["raw_ext"].remove(del_raw_extension)

            except ValueError:
                pass

        # Print new settings
        print(
            "\n"
            f"Safe String: {new_settings['safe_string']}\n"
            f"Space letter: {new_settings['space_letter']}\n"
            f"Image extensions: {new_settings['image_ext']}\n"
            f"Raw extensions: {new_settings['raw_ext']}\n"
            f"Raw renaming: {new_settings['raw_rename']}\n"
        )

        # Confirm new settings
        confirm = input(f"Do you confirm settings ? [y/n]")

        if confirm == "y":

            # Save new settings into json file
            self.settings_objects.save_settings(new_settings)
            self.rename_object.update_settings(new_settings)

        else:
            print(Fore.RED + f"New settings were not saved.\n" + Fore.RESET)

    def help(self):
        print(
            Fore.BLUE
            + f'"rename"'
            + Fore.RESET
            + f" - renames all images in a folder structure\n"
            + Fore.BLUE
            + f'"settings"'
            + Fore.RESET
            + f" - change settings\n"
            + Fore.BLUE
            + f'"quit"'
            + Fore.RESET
            + f" - quits the application\n"
            + Fore.LIGHTMAGENTA_EX
            + f"\nFor more Help please visit https://github.com/jolsfd/imagenamer/ \n"
            + Fore.RESET
        )
