class Config:
    """a class to validate the user config"""

    def __init__(self, args_obj):
        self.origin_path = str(args_obj.origin)
        self.destination_path = str(args_obj.destination)
        self.include_hidden = bool(args_obj.hidden)

    def validate(self):
        pass
