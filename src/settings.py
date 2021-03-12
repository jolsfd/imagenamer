import os, json

class Settings:
    def __init__(self, path_to_settings):
        self.path_to_settings = path_to_settings
        self.settings_template = {
            'safe_string':'IMG',
            'file_ext':['.jpg'],
            'space_letter':'_'
        }

    def save_settings(self, settings):
        try:
            json_file = open(self.path_to_settings, 'w')

            json.dump(settings, json_file)

            json_file.close()

            print('Saved Changes into json file.')

        except:
            print('Settings could not be saved') # print red

    def load_settings(self):
        try:
            json_file = open(self.path_to_settings ,'r')

            settings = json.load(json_file)

            json_file.close()

            return settings
        except FileNotFoundError:
            self.save_settings(self.settings_template)

            return self.settings_template

    def check_settings(self, settings):
        error = False

        try:
            if type(settings['safe_string']) != type(str()):
                error = True

            if type(settings['file_ext']) != type(list()):
                error = True

            if type(settings['space_letter']) != type(str()):
                error = True

        except AttributeError:
            print('Could not find all Settings. Please visit https://github.com/jolsfd/imagenamer') # print red
            error = True

        if error:
            print('Error in settings. Please visit https://github.com/jolsfd/imagenamer') # print red

        return error