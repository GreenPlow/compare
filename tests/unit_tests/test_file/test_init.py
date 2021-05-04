from compare import file
import pytest


class TestClass:
    test_filename = "afilename"
    test_path = "apath"

    def test_create_File_instance(self):
        """should create a new instance of File when provided arguments"""
        # given:
        File = file.File

        # when:
        test_file_object = File(self.test_filename, self.test_path)

        # then assert:
        assert type(test_file_object.filename) is str
        assert test_file_object.filename == self.test_filename

        assert type(test_file_object.path) is str
        assert test_file_object.path == self.test_path

        assert type(test_file_object.kMDItemFSName) is type(None)
        assert type(test_file_object.kMDItemFSSize) is type(None)
        assert type(test_file_object.kMDItemKind) is type(None)
        assert type(test_file_object.kMDItemPhysicalSize) is type(None)
        assert type(test_file_object.kMDItemLogicalSize) is type(None)

    def test_create_OriginFile_instance(self):
        """should create a new instance of Origin when provided arguments"""

        # given:
        OriginFile = file.OriginFile

        # when:
        test_file_object = OriginFile(self.test_filename, self.test_path)

        # then assert:
        assert type(test_file_object.filename) is str
        assert test_file_object.filename == self.test_filename

        assert type(test_file_object.path) is str
        assert test_file_object.path == self.test_path

        assert type(test_file_object.location) is str
        assert test_file_object.location == "origin"

        assert type(test_file_object.kMDItemFSName) is type(None)
        assert type(test_file_object.kMDItemFSSize) is type(None)
        assert type(test_file_object.kMDItemKind) is type(None)
        assert type(test_file_object.kMDItemPhysicalSize) is type(None)
        assert type(test_file_object.kMDItemLogicalSize) is type(None)
