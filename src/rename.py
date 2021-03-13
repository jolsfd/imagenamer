import os
from exif import Image

class Rename:
    def __init__(self, settings):
        self.settings = settings

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
            os.rename(old_file,new_file)

    def collect_files(self,path_to_files):
        files = []
        #other_file

        for root, dirnames, filenames in os.walk(path_to_files):
            for file in filenames:
                # check safe string
                if file[:len(self.settings['safe_string'])] == self.settings['safe_string']:
                    continue

                # check file extension
                file_ext = os.path.splitext(file)[1]

                if file_ext in self.settings['file_ext']:
                    files.append(os.path.join(root, file))

                #else:
                    #other_file.append

        del dirnames

        return files #other_file

    def rename_images(self,file_list):
        for old_file in file_list:
            head, old_tail = os.path.split(old_file)

            old_filename, file_ext = os.path.splitext(old_tail)

            with open(old_file, 'rb'):
                image_object = Image(old_file)

            if image_object.has_exif():
                new_filename = self.new_filename(image_object)

                # if raw
                # check other list

                new_file = os.path.join(head, new_filename + file_ext)

                if os.path.isfile(new_file):
                    self.rename_image_copy(old_file,head,new_filename,file_ext,2)

                if os.path.isfile(old_file):
                    # rename file
                    os.rename(old_file, new_file)

                else:
                    print('{} was not found'.format(old_tail)) # print red

            else:
                print('{} has no exif'.format(old_tail)) # red
