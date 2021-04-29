import pytest
from compare import config


class FakeParseArgs:
    """Example of an object returned from args_helper.parse_args"""

    __test__ = False  # Stops pytest from warning that it cannot instantiate this class

    def __init__(self, origin, destination, hidden):
        self.origin = origin
        self.destination = destination
        self.hidden = hidden


test_args_object_default = FakeParseArgs(
    "something/directory_A", "something/directory_B", False
)
test_args_object_hidden_files = FakeParseArgs(
    "something/directory_A", "something/directory_B", True
)


class TestClass:
    def test_issamepath_true(self, mocker, mock_os, mock_print):
        """should return true if the paths are the same"""

        # given:
        args_object_default = FakeParseArgs(
            "something/directory_A", "something/directory_A", False
        )
        test_config = config.Config(args_object_default)

        # when:
        actual = test_config.issamepath()

        # then assert:
        mock_print.assert_called_once_with(
            "\nSTOP... The origin and destination paths are the same.\n"
        )
        assert actual == True

    def test_issamepath_false(self, mocker, mock_os, mock_print):
        """should return false if both paths are different"""

        # given
        mock_os.path.samefile.return_value = False

        args_object_default = FakeParseArgs(
            "something/directory_A", "something/directory_B", False
        )
        test_config = config.Config(args_object_default)

        # when:
        actual = test_config.issamepath()

        # then assert:
        mock_print.assert_not_called()
        assert actual == False