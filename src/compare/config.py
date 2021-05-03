import os


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