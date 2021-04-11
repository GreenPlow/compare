import os


class File:
    """a class to hold file meta data gathered from the mdls command"""
    src = str(None)
    dest = str(None)
    hidden = bool(None)

    def __init__(self, filename, location):
        self.filename = filename
        self.location = location  # define if this file is located in the src or dest
        self.kMDItemFSName = None
        self.kMDItemFSSize = None
        self.kMDItemKind = None
        self.kMDItemPhysicalSize = None
        self.kMDItemLogicalSize = None

    @staticmethod
    def checkif_pathsaredupes():
        if os.path.samefile(File.src, File.dest):
            # TODO ADD TEST
            print("STOP... The src and dest paths are the same.")
            return True

    @staticmethod
    def checkif_pathsdonotexist():
        dict = {'src': File.src, 'dest': File.dest}
        for path in dict:
            if os.path.isdir(dict[path]):
                continue
            else:
                print(f'STOP... \'{path}\' \'{dict[path]}\' is not a dir')
                return True
