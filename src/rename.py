import os
from exif import Image
from colorama import Fore, Back, Style
from datetime import datetime


class Rename:
    def __init__(self, settings):
        self.settings = settings
        self.image_list = []
        self.raw_list = []

    def build_file_dict(self, source_name):
        file_dict = {}

        # Insert data into dictonary
        file_dict["source_name"] = source_name
        file_dict["head"], file_dict["tail"] = os.path.split(source_name)
        file_dict["filename"], file_dict["file_ext"] = os.path.splitext(
            file_dict["tail"]
        )
        file_dict["new_filename"] = ""
        file_dict["new_tail"] = ""
        file_dict["target_name"] = ""
        file_dict["number_of_copy"] = 1

        return file_dict

    def exif_data(self, image_exif):
        try:
            exif_datetime = image_exif.datetime_original
            datetime_object = datetime.strptime(exif_datetime, "%Y:%m:%d %H:%M:%S")

            model = image_exif.model.replace(" ", "")

            return datetime_object, model

        except:
            return None

    def new_filename(self, image_exif):
        if self.exif_data(image_exif) == None:
            return None

        else:
            datetime_object, model = self.exif_data(image_exif)

            new_filename = (
                self.settings["format"]
                .replace("$Y", datetime_object.year)
                .replace("$M", datetime_object.month)
                .replace("$D", datetime_object.day)
                .replace("$h", datetime_object.hour)
                .replace("$m", datetime_object.minute)
                .replace("$s", datetime_object.second)
                .replace("MODEL", model)
            )

            return new_filename

    def rename(self, file_dict):
        while os.path.isfile(file_dict["target_name"]):
            file_dict["number_of_copy"] = file_dict["number_of_copy"] + 1
            file_dict["new_tail"] = (
                file_dict["new_filename"]
                + "~"
                + str(file_dict["number_of_copy"])
                + file_dict["file_ext"]
            )
            file_dict["target_name"] = os.path.join(
                file_dict["head"], file_dict["new_tail"]
            )

        if os.path.isfile(file_dict["source_name"]):
            os.rename(file_dict["source_name"], file_dict["target_name"])
            print(
                Fore.GREEN
                + f"{file_dict['tail']} -> {file_dict['new_tail']}"
                + Fore.RESET
            )

        else:
            print(Fore.RED + f"{file_dict['tail']} was not found" + Fore.RESET)

    def collect_files(self, path_to_files, excluded_folders):
        for root, dirnames, file_list in os.walk(path_to_files):
            # Exclude folders
            for dirname in dirnames:
                if dirname in excluded_folders:
                    dirnames.remove(dirname)
                    print(Fore.RED + f"Exclude folder: {dirname}" + Fore.RESET)

            # Get images
            for file in file_list:
                # Check safe rename
                if self.settings["safe_rename"]:
                    # Check safe string
                    if (
                        file[: len(self.settings["safe_string"])]
                        == self.settings["safe_string"]
                    ):
                        continue

                # check file extension
                file_ext = os.path.splitext(file)[1]

                if file_ext in self.settings["image_ext"]:
                    self.image_list.append(os.path.join(root, file))

                elif file_ext in self.settings["raw_ext"]:
                    self.raw_list.append(os.path.join(root, file))

        del dirnames

        return len(self.image_list), len(self.raw_list)

    def rename_raws(self, image_filename, new_image_filename):
        for source_name in self.raw_list:
            raw_dict = self.build_file_dict(source_name)

            if raw_dict["filename"] == image_filename:
                raw_dict["new_filename"] = new_image_filename
                raw_dict["new_tail"] = raw_dict["new_filename"] + raw_dict["file_ext"]
                raw_dict["target_name"] = os.path.join(
                    raw_dict["head"], raw_dict["new_tail"]
                )

                self.rename(raw_dict)

                self.raw_list.remove(source_name)

            del raw_dict

    def rename_image(self, source_name):
        image_dict = self.build_file_dict(source_name)

        with open(source_name, "rb") as image:
            image_exif = Image(image)

        if image_exif.has_exif:
            image_dict["new_filename"] = self.new_filename(image_exif)

            if image_dict["new_filename"] != None:
                image_dict["new_tail"] = (
                    image_dict["new_filename"] + image_dict["file_ext"]
                )
                image_dict["target_name"] = os.path.join(
                    image_dict["head"], image_dict["new_tail"]
                )

                if self.settings["raw_rename"]:
                    self.rename_raws(image_dict["filename"], image_dict["new_filename"])

                self.rename(image_dict)

            else:
                print(
                    Fore.RED
                    + f"{image_dict['tail']} has no datetime and model exif tags"
                    + Fore.RESET
                )

        else:
            print(Fore.RED + f"{image_dict['tail']} has no exif data" + Fore.RESET)

        # delete variables for free memory space
        del image_dict
        del image_exif

    def rename_images(self):
        for source_name in self.image_list:
            self.rename_image(source_name)

    def clear(self):
        self.image_list = []
        self.raw_list = []

    def update_settings(self, new_settings):
        self.settings = new_settings