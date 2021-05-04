class File:
    """a class to hold file meta data gathered from the mdls command"""

    def __init__(self, filename, path):
        self.filename = filename
        self.path = path
        self.kMDItemFSName = None
        self.kMDItemFSSize = None
        self.kMDItemKind = None
        self.kMDItemPhysicalSize = None
        self.kMDItemLogicalSize = None
