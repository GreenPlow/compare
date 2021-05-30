import os
from compare import config, file
from tests.unit_tests.test_config.shared_classes import FakeParseArgs


class TestClass:
    def test_get_origin_files_and_exclude_sub_dirs(self, tmpdir):
        """should return a list of objects for files located in the origin directory.
        Test uses a tmpdir fixture from pytest. The tempdir for the last three test invocations is maintained.
        Avoid mocking OS for this test so that list comprehension returns objects."""

        # given two files in an origin directory and a sub directory
        origin_path = tmpdir.mkdir("someorigindir")
        filenameOne = "file1.txt"
        filenameTwo = "file2.txt"
        subdirectory = origin_path.mkdir("child")

        thefullpathOne = origin_path.join(filenameOne)
        thefullpathOne.write("content")
        thefullpathTwo = origin_path.join(filenameTwo)
        thefullpathTwo.write("content")

        destination_path = tmpdir.mkdir("somedestinationdir")

        args_object_new = FakeParseArgs(origin_path, destination_path, False)
        config_under_test = config.Config(args_object_new)

        print("temp dir for test:", config_under_test.origin_path)
        print("test subdirectory", subdirectory)
        print("files in the temp test dir:", os.listdir(config_under_test.origin_path))

        # when
        actual = config_under_test.get_origin_files()

        # then get back a list of objects, one object for each origin file
        assert isinstance(actual[0], file.OriginFile)
        assert isinstance(actual[1], file.OriginFile)
        assert len(actual) is 2

        assert actual[0].path == origin_path
        assert actual[1].path == origin_path

        # Note that listdir does not return an ordered list and may be impacted by the OS
        # Was able to pass the test locally, but then failed when running in the cloud
        # Conditional below should allow it to be independant of OS

        if actual[0].filename == filenameOne:
            assert actual[1].filename == filenameTwo
        elif actual[0].filename == filenameTwo:
            assert actual[1].filename == filenameOne
        else:
            assert False is True

    def test_get_origin_files_exclude_hidden_files(self, tmpdir):
        """should return a list of objects for files located in the origin directory, excluding the hidden file"""

        # given three files in an origin directory
        origin_path = tmpdir.mkdir("someorigindir")
        filenameOne = "file1.txt"
        filenameTwo = ".file2.txt"
        filenameThree = "file3.txt"

        thefullpathOne = origin_path.join(filenameOne)
        thefullpathOne.write("content")
        thefullpathTwo = origin_path.join(filenameTwo)
        thefullpathTwo.write("content")
        thefullpathThree = origin_path.join(filenameThree)
        thefullpathThree.write("content")

        destination_path = tmpdir.mkdir("somedestinationdir")

        args_object_new = FakeParseArgs(origin_path, destination_path, False)
        config_under_test = config.Config(args_object_new)

        print("temp dir for test:", config_under_test.origin_path)
        print("files in the temp test dir:", os.listdir(config_under_test.origin_path))

        # when
        actual = config_under_test.get_origin_files()

        # then get back a list of objects, one object for each origin file that was not a hidden file
        assert isinstance(actual[0], file.OriginFile)
        assert isinstance(actual[1], file.OriginFile)
        assert len(actual) is 2

        assert actual[0].path == origin_path
        assert actual[1].path == origin_path

        # Note that listdir does not return an ordered list and may be impacted by the OS
        # Was able to pass the test locally, but then failed when running in the cloud
        # Conditional below should allow it to be independant of OS

        if actual[0].filename == filenameOne:
            assert actual[1].filename == filenameThree
        elif actual[0].filename == filenameThree:
            assert actual[1].filename == filenameOne
        else:
            assert False is True

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

        # Note that listdir does not return an ordered list and may be impacted by the OS
        # Was able to pass the test locally, but then failed when running in the cloud
        # Conditional below should allow it to be independant of OS

        if actual[0].filename == filenameOne:
            assert actual[1].filename == filenameTwo
        elif actual[0].filename == filenameTwo:
            assert actual[1].filename == filenameOne
        else:
            assert False is True
