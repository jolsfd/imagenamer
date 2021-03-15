import os
from exif import Image

class Rename:
    def __init__(self, settings):
        self.settings = settings
        self.image_list = []
        self.raw_list = []

    def get_file_data(self, source_name):
        head, tail = os.path.split(source_name)
        filename, file_ext = os.path.splitext(tail)

        return head, file_ext, filename, tail

    def new_filename(self, image_object):
        space_letter = self.settings['space_letter']
        datetime = image_object.datetime_original().replace(':','').replace(' ',space_letter)
        model = image_object.model().replace(' ','')

        new_filename = self.settings['safe_string'] + space_letter + datetime + space_letter + model

        return new_filename

    def rename_image_copy(self,old_file,head,new_filename,file_ext,number_of_copy):
        new_file = os.path.join(head, new_filename + '~' + str(number_of_copy) + file_ext)

        if os.path.isfile(new_file):
            self.rename_image_copy(old_file,head,new_filename,file_ext,number_of_copy + 1)

        else:
            if os.path.isfile(old_file):
                os.rename(old_file,new_file)

    def collect_files(self,path_to_files):
        for root, dirnames, file_list in os.walk(path_to_files):
            for file in file_list:
                # check safe string
                if file[:len(self.settings['safe_string'])] == self.settings['safe_string']:
                    continue

                # check file extension
                file_ext = os.path.splitext(file)[1]

                if file_ext in self.settings['image_ext']:
                    self.image_list.append(os.path.join(root, file))

                elif file_ext in self.settings['raw_ext']:
                    self.raw_list.append(os.path.join(root,file))

        del dirnames

    def raw_rename(self, image_filename, new_filename):
        for source_name in self.raw_list:
            head, file_ext, filename, tail = self.get_file_data(source_name)

            if filename == image_filename:
                new_tail = new_filename + file_ext
                target_name = os.path.join(head, new_tail)
            
                # Rename file
                if os.path.isfile(target_name):
                    print(F'{new_tail} exists already') # TODO: Better copy renaming

                elif os.path.isfile(source_name) and not os.path.isfile(target_name):
                    os.rename(source_name, target_name)
                    self.raw_list.remove(source_name)
                    print(F'{tail} -> {new_tail}')

                else:
                    print(F'{tail} was not found') # print red

    def rename_images(self):
        for source_name in self.image_list:
            head, file_ext, filename, tail = self.get_file_data(source_name)
    
            with open(source_name, 'rb'):
                image_object = Image(source_name)

            if image_object.has_exif():
                # Build new file data
                new_filename = self.new_filename(image_object)
                new_tail = new_filename + file_ext
                target_name = os.path.join(head, new_tail)

                if self.settings['raw_renaming']:
                    self.raw_rename(filename, new_filename)

                # Rename file
                if os.path.isfile(target_name):
                    print(F'{new_tail} exists already') # TODO: Better copy renaming

                elif os.path.isfile(source_name) and not os.path.isfile(target_name):
                    os.rename(source_name, target_name)
                    print(F'{tail} -> {new_tail}') # green

                else:
                    print(F'{tail} was not found')# print red

            else:
                print(F'{tail} has no exif') # red

    def clear(self):
        self.image_list = []
        self.raw_list = []

    def update_settings(self, new_settings):
        self.settings = new_settings