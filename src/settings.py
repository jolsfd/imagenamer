import os, json
from colorama import Fore, Back, Style


class Settings:
    def __init__(self, path_to_settings):
        self.path_to_settings = path_to_settings
        self.settings_template = {
            "safe_string": "IMG",
            "image_ext": [".jpg", ".JPG", ".jpeg", ".JPEG"],
            "space_letter": "_",
            "raw_rename": True,
            "safe_rename": True,
            "raw_ext": [".raw", ".cr2", ".dng"],
        }

    def save_settings(self, new_settings):
        try:
            json_file = open(self.path_to_settings, "w")

            json.dump(new_settings, json_file)

            json_file.close()

            print(Fore.GREEN + f"Saved Changes into json file.\n" + Fore.RESET)

        except:
            print(Fore.RED + f"Settings could not be saved\n" + Fore.RESET)

    def load_settings(self):
        try:
            json_file = open(self.path_to_settings, "r")

            settings = json.load(json_file)

            json_file.close()

            return settings
        except FileNotFoundError:
            self.save_settings(self.settings_template)

            return self.settings_template

    def check_settings(self, settings):
        error = False

        try:
            if type(settings["safe_string"]) != type(str()):
                error = True

            if type(settings["space_letter"]) != type(str()):
                error = True

            if type(settings["raw_rename"]) != type(bool()):
                error = True

            if type(settings["safe_reanme"]) != type(bool()):
                error = True

            if type(settings["image_ext"]) != type(list()):
                error = True

            else:
                for imgage_ext in settings["image_ext"]:
                    if type(imgage_ext) != type(str()):
                        error = True

            if type(settings["raw_ext"]) != type(list()):
                error = True

            else:
                for raw_ext in settings["raw_ext"]:
                    if type(raw_ext) != type(str()):
                        error = True

        except AttributeError:
            error = True

        if error:
            print(
                Fore.RED
                + f"Error in settings. Please visit https://github.com/jolsfd/imagenamer \n"
                + Fore.RESET
            )

        return error
