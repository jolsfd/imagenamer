import os
from exif import Image

class Rename:
    def __init__(self, settings):
        self.settings = settings

    def new_filename(self, path_to_file):
        with open(path_to_file, 'rb') as image_file:
            image_exif = Image(path_to_file)

        if image_exif.has_exif:    
            space_letter = self.settings['space_letter']
            datetime = image_exif.datetime_original().replace(':','').replace(' ',space_letter)
            model = image_exif.model().replace(' ','')

            new_filename = self.settings['safe_string'] + space_letter + datetime + space_letter + model

            return new_filename

    #def rename_image_copy(old_filename,new_filename)

    def collect_files(self,path_to_files):
        files = []

        for root, dirnames, filenames in os.walk(path_to_files):
            for file in filenames:
                # check safe string
                if file[:len(self.settings['safe_string'])] == self.settings['safe_string']:
                    continue

                # check file extension
                file_ext = os.path.splitext(file)[1]

                if file_ext in self.settings['file_ext']:
                    files.append(os.path.join(root, file))

        del dirnames

        return files