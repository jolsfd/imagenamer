import os
from exif import Image
from colorama import Fore, Back, Style

class Rename:
    def __init__(self, settings):
        self.settings = settings
        self.image_list = []
        self.raw_list = []

#    def get_file_data(self, source_name):
#        head, tail = os.path.split(source_name)
#        filename, file_ext = os.path.splitext(tail)
#
#        return head, file_ext, filename, tail
#
#    def new_filename(self, image_object):
#        try:
#            space_letter = self.settings['space_letter']
#            datetime = image_object.datetime_original.replace(':','').replace(' ',space_letter)
#            model = image_object.model.replace(' ','')
#
#            new_filename = self.settings['safe_string'] + space_letter + datetime + space_letter + model
#
#            return new_filename
#        
#        except:
#            return None

    def build_file_dict(self, source_name):
        file_dict = {}

        # Insert data into dictonary
        file_dict['source_name'] = source_name
        file_dict['head'], file_dict['tail'] = os.path.split(source_name)
        file_dict['filename'], file_dict['file_ext'] = os.path.splitext(file_dict['tail'])
        file_dict['new_filename'] = ''
        file_dict['new_tail'] = ''
        file_dict['target_name'] = ''
        file_dict['number_of_copy'] = 1

        return file_dict

    def exif_filename(self, image_exif):
        try:
            datetime = image_exif.datetime_original.replace(':','').replace(' ',self.settings['space_letter'])
            model = image_exif.model.replace(' ','')

            new_filename = self.settings['safe_string'] + self.settings['space_letter'] + datetime + self.settings['space_letter'] + model

            return new_filename

        except:
            return None

    def rename(self, file_dict):
        while os.path.isfile(file_dict['target_name']):
            file_dict['number_of_copy'] = file_dict['number_of_copy'] + 1
            file_dict['new_tail'] = file_dict['new_filename'] + '~' + str(file_dict['number_of_copy']) + file_dict['file_ext']
            file_dict['target_name'] = os.path.join(file_dict['head'], file_dict['new_tail'])

        if os.path.isfile(file_dict['source_name']):
            os.rename(file_dict['source_name'], file_dict['target_name'])
            print(Fore.GREEN + F"{file_dict['tail']} -> {file_dict['new_tail']}" + Fore.RESET)

        else:
            print(Fore.RED + F"{file_dict['tail']} was not found" + Fore.RESET)

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

        return len(self.image_list), len(self.raw_list)

#    def raw_rename(self, image_filename, new_filename):
#        for source_name in self.raw_list:
#            head, file_ext, filename, tail = self.get_file_data(source_name)
#
#            if filename == image_filename:
#                new_tail = new_filename + file_ext
#                target_name = os.path.join(head, new_tail)
#            
#                # Rename file
#                if os.path.isfile(target_name):
#                    print(F'{new_tail} exists already') # TODO: Better copy renaming
#                    #file_name = self.rename_image_copy(target_name,1)
#                    #print(F'{tail} -> {os.path.split(file_name)[1]}')
#
#                elif os.path.isfile(source_name) and not os.path.isfile(target_name):
#                    os.rename(source_name, target_name)
#                    self.raw_list.remove(source_name)
#                    print(F'{tail} -> {new_tail}')
#
#                else:
#                    print(F'{tail} was not found') # print red

    def rename_raws(self, image_filename, new_image_filename):
        for source_name in self.raw_list:
            raw_dict = self.build_file_dict(source_name)

            if raw_dict['filename'] == image_filename:
                raw_dict['new_filename'] = new_image_filename
                raw_dict['new_tail'] = raw_dict['new_filename'] + raw_dict['file_ext']
                raw_dict['target_name'] = os.path.join(raw_dict['head'], raw_dict['new_tail'])

                self.rename(raw_dict)

                self.raw_list.remove(source_name)

            del raw_dict

    def rename_image(self, source_name):
        image_dict = self.build_file_dict(source_name)

        with open(source_name, 'rb') as image:
            image_exif = Image(image)

        if image_exif.has_exif:
            image_dict['new_filename'] = self.exif_filename(image_exif)

            if image_dict['new_filename'] != None:
                image_dict['new_tail'] = image_dict['new_filename'] + image_dict['file_ext']
                image_dict['target_name'] = os.path.join(image_dict['head'], image_dict['new_tail'])

                if self.settings['raw_rename']:
                    self.rename_raws(image_dict['filename'], image_dict['new_filename'])

                self.rename(image_dict)

            else:
                print(Fore.RED + F"{image_dict['tail']} has no datetime and model exif tags" + Fore.RESET)

        else:
            print(Fore.RED + F"{image_dict['tail']} has no exif data" + Fore.RESET)

        #delete variables for free memory space
        del image_dict
        del image_exif

#    def rename_images(self):
#       for source_name in self.image_list:
#            head, file_ext, filename, tail = self.get_file_data(source_name)
#    
#            with open(source_name, 'rb') as image:
#                image_object = Image(image)
#
#            if image_object.has_exif:
#                # Build new file data
#                number_of_copy = 1
#                new_filename = self.new_filename(image_object)
#
#                if new_filename == None:
#                    print(F'{tail} has no datetime and model exif')
#                    continue
#
#                new_tail = new_filename + file_ext
#                target_name = os.path.join(head, new_tail)
#
#                if self.settings['raw_rename']:
#                    self.raw_rename(filename, new_filename)
#
#                while os.path.isfile(target_name):
#                    number_of_copy = number_of_copy + 1
#                    new_tail = new_filename + '~' + str(number_of_copy) + file_ext
#                    target_name = os.path.join(head, new_tail)
#
#                if os.path.isfile(source_name) and not os.path.isfile(target_name):
#                    os.rename(source_name, target_name)
#                    print(F'{tail} -> {new_tail}') # green
#
#               else:
#                    print(F'{tail} was not found')# print red
#
#            else:
#                print(F'{tail} has no exif') # red

    def rename_images(self):
        for source_name in self.image_list:
            self.rename_image(source_name)

    def clear(self):
        self.image_list = []
        self.raw_list = []

    def update_settings(self, new_settings):
        self.settings = new_settings