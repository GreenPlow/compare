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
        pass

    def isvalid(self):
        self.issamepath()
        pass
