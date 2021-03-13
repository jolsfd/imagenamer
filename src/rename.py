import os
from exif import Image

class Rename:
    def __init__(self, settings):
        self.settings = settings

    def get_file_data(self,file):
        head, tail = os.path.split(file)
        filename, file_ext = os.path.splitext(tail)

        return head, filename, file_ext

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
        files = []
        other_files = []

        for root, dirnames, filenames in os.walk(path_to_files):
            for file in filenames:
                # check safe string
                if file[:len(self.settings['safe_string'])] == self.settings['safe_string']:
                    continue

                # check file extension
                file_ext = os.path.splitext(file)[1]

                if file_ext in self.settings['file_ext']:
                    files.append(os.path.join(root, file))

                else:
                    other_files.append(os.path.join(root,file))

        del dirnames

        return files, other_files

    def rename_images(self,file_list,other_file_list):
        for old_file in file_list:
            head, old_tail = os.path.split(old_file)

            old_filename, file_ext = os.path.splitext(old_tail)

            with open(old_file, 'rb'):
                image_object = Image(old_file)

            if image_object.has_exif():
                new_filename = self.new_filename(image_object)

                if self.settings['raw_renaming']:
                    self.rename_raw()

                new_file = os.path.join(head, new_filename + file_ext)

                if os.path.isfile(new_file):
                    self.rename_image_copy(old_file,head,new_filename,file_ext,2)

                if os.path.isfile(old_file):
                    # rename file
                    os.rename(old_file, new_file)

                    # Visualization

                else:
                    print('{} was not found'.format(old_tail)) # print red

            else:
                print('{} has no exif'.format(old_tail)) # red

    def rename_image(self,old_file):
        head, old_filename, file_ext = self.get_file_data(old_file)
    
        with open(old_file, 'rb'):
            image_object = Image(old_file)

        if image_object.has_exif():
            new_filename = self.new_filename(image_object)

            #if self.settings['raw_renaming']:
                #self.rename_raw()

            new_file = os.path.join(head, new_filename + file_ext)

            if os.path.isfile(new_file):
                self.rename_image_copy(old_file,head,new_filename,file_ext,2)

            if os.path.isfile(old_file):
                # rename file
                os.rename(old_file, new_file)

                print('{old_tail} -> {new_tail}'.format(old_tail=old_filename + file_ext, new_tail=new_filename + file_ext))

            else:
                print('{} was not found'.format(old_filename + file_ext)) # print red

        else:
            print('{} has no exif'.format(old_filename + file_ext)) # red