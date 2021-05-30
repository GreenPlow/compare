import os
from compare.file import OriginFile as newOriginFileObject


class Config:
    """a class to validate the user config"""

    def __init__(self, args_obj):
        self.origin_path = str(args_obj.origin)
        self.destination_path = str(args_obj.destination)
        self.include_hidden = bool(args_obj.hidden)

    def issamepath(self):
        if os.path.samefile(self.origin_path, self.destination_path):
            print("\nSTOP... The origin and destination paths are the same.\n")
            return True
        return False

    def isbadpath(self):
        dictionary = {"origin": self.origin_path, "destination": self.destination_path}
        for key in dictionary:
            if os.path.isdir(dictionary[key]):
                continue
            else:
                print(f"\nSTOP... '{dictionary[key]}' is not a dir\n")
                return True
        return False

    def printpaths(self):
        print("path to copy files from...", self.origin_path)
        print("path to put copied files...", self.destination_path, "\n")

    def isvalid(self):
        if self.issamepath():
            return False
        elif self.isbadpath():
            return False
        else:
            self.printpaths()
            return True

    def get_origin_files(self):
        """Return a list of objects. Each object represents a single file. Do not make objects for sub directories."""

        if self.include_hidden:
            print("...including hidden files")
            return ["hold"]
        else:
            "list comprehension"
            return [
                newOriginFileObject(filename, self.origin_path)
                for filename in os.listdir(self.origin_path)
                if not filename.startswith(".")
                and os.path.isfile(os.path.join(self.origin_path, filename))
            ]
