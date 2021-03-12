import os, json

class Settings:
    def __init__(path_to_settings):
        self.path_to_settings = path_to_settings
        self.settings_template = {
            'safe_string':'IMG',
            'file_ext':['.jpg'],
            'space_letter':'_'
        }