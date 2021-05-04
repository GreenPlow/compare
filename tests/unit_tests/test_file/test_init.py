from compare.file import File
import pytest


def test_create_File_instance():
    """should create a new instance of File when provided arguments"""
    # given:
    test_filename = "afilename"
    test_path = "apath"

    # when:
    test_file_object = File(test_filename, test_path)

    # then assert:
    assert type(test_file_object.filename) is str
    assert test_file_object.filename == test_filename

    assert type(test_file_object.path) is str
    assert test_file_object.path == test_path

    assert type(test_file_object.kMDItemFSName) is type(None)
    assert type(test_file_object.kMDItemFSSize) is type(None)
    assert type(test_file_object.kMDItemKind) is type(None)
    assert type(test_file_object.kMDItemPhysicalSize) is type(None)
    assert type(test_file_object.kMDItemLogicalSize) is type(None)
