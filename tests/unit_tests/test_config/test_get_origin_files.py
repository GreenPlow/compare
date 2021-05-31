import os, pytest
from compare import config, file
from tests.unit_tests.test_config.shared_classes import FakeParseArgs

# These tests use the tmpdir fixture from pytest. The tempdir for the last three test invocations is maintained.
# Avoid mocking os for these tests so that os.listdir() in the prod code can evaluate the fake files and directories.

# Note that listdir does not return an ordered list and may be impacted by the OS.
# Conditional asserts should allow tests to run on linux, mac, windows os without issue from the filesystem.
class TestScenario:
    """Example of an object returned from args_helper.parse_args"""

    __test__ = False  # Stops pytest from warning that it cannot instantiate this class

    def __init__(self, hidden, filename_list, expected_len):
        self.hidden = hidden
        self.filename_list = filename_list
        self.expected_len = expected_len


class TestClass:

    # def test_get_origin_files_and_exclude_sub_dirs(self, tmpdir):
    #     """should return a list of objects for files located in the origin directory."""

    #     # given two files in an origin directory and a sub directory
    #     origin_path = tmpdir.mkdir("someorigindir")
    #     filenameOne = "file1.txt"
    #     filenameTwo = "file2.txt"
    #     subdirectory = origin_path.mkdir("child")

    #     thefullpathOne = origin_path.join(filenameOne)
    #     thefullpathOne.write("content")
    #     thefullpathTwo = origin_path.join(filenameTwo)
    #     thefullpathTwo.write("content")

    #     destination_path = tmpdir.mkdir("somedestinationdir")

    #     args_object_new = FakeParseArgs(origin_path, destination_path, False)
    #     config_under_test = config.Config(args_object_new)

    #     print("temp dir for test:", config_under_test.origin_path)
    #     print("test subdirectory", subdirectory)
    #     print("files in the temp test dir:", os.listdir(config_under_test.origin_path))

    #     # when
    #     actual = config_under_test.get_origin_files()

    #     # then get back a list of objects, one object for each origin file
    #     assert isinstance(actual[0], file.OriginFile)
    #     assert isinstance(actual[1], file.OriginFile)
    #     assert len(actual) is 2

    #     assert actual[0].path == origin_path
    #     assert actual[1].path == origin_path

    #     if actual[0].filename == filenameOne:
    #         assert actual[1].filename == filenameTwo
    #     elif actual[0].filename == filenameTwo:
    #         assert actual[1].filename == filenameOne
    #     else:
    #         assert False is True

    exclude_hidden_files = TestScenario(False, ["file1.txt", ".file2.txt", "file3.txt"], 2)
    include_hidden_files = TestScenario(True, ["file1.txt", ".file2.txt", "file3.txt"], 3)

    @pytest.mark.parametrize(
    "test_input", [exclude_hidden_files, include_hidden_files])
    def test_get_origin_files_with_no_sub_dir(self, test_input, tmpdir):
        """should return a list of objects for files located in the origin directory, excluding the hidden file"""

        # given three files in an origin directory
        origin_path = tmpdir.mkdir("someorigindir")

        for filename in test_input.filename_list:
            fullpath = origin_path.join(filename)
            fullpath.write("content")

        destination_path = tmpdir.mkdir("somedestinationdir")

        args_object_new = FakeParseArgs(origin_path, destination_path, test_input.hidden)
        config_under_test = config.Config(args_object_new)

        print("temp dir for test:", config_under_test.origin_path)
        print("files in the temp test dir:", os.listdir(config_under_test.origin_path))

        # when
        result = config_under_test.get_origin_files()

        # then get back a list of objects, one object for each origin file that was not a hidden file
        assert len(result) is test_input.expected_len

        for resultObject in result:
            assert isinstance(resultObject, file.OriginFile)
            assert resultObject.path == origin_path
            assert test_input.filename_list.count(resultObject.filename)

    def test_get_origin_files_include_hidden_files(self, tmpdir):
        """should return a list of objects for files located in the origin directory, including the hidden file. Sub directories should be excluded"""

        # given two files in an origin directory and a sub directory
        origin_path = tmpdir.mkdir("someorigindir")
        filenameOne = "file1.txt"
        filenameTwo = ".file2.txt"
        subdirectory = origin_path.mkdir("child")

        thefullpathOne = origin_path.join(filenameOne)
        thefullpathOne.write("content")
        thefullpathTwo = origin_path.join(filenameTwo)
        thefullpathTwo.write("content")

        destination_path = tmpdir.mkdir("somedestinationdir")

        args_object_new = FakeParseArgs(origin_path, destination_path, True)
        config_under_test = config.Config(args_object_new)

        print("temp dir for test:", config_under_test.origin_path)
        print("test subdirectory", subdirectory)
        print("files in the temp test dir:", os.listdir(config_under_test.origin_path))

        # when
        actual = config_under_test.get_origin_files()

        # then get back a list of objects, one object for each origin file including the hidden file
        assert isinstance(actual[0], file.OriginFile)
        assert isinstance(actual[1], file.OriginFile)
        assert len(actual) is 2

        assert actual[0].path == origin_path
        assert actual[1].path == origin_path

        if actual[0].filename == filenameOne:
            assert actual[1].filename == filenameTwo
        elif actual[0].filename == filenameTwo:
            assert actual[1].filename == filenameOne
        else:
            assert False is True
