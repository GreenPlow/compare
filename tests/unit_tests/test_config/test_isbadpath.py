import pytest
from compare import config
from tests.unit_tests.test_config.shared_classes import FakeParseArgs


class TestClass:
    def test_isbadpath_true(self, mock_os, mock_print):
        """should return true if either path specified is not a real path"""

        # given:
        mock_os.path.isdir.side_effect = [True, False]
        args_object_default = FakeParseArgs(
            "something/directory_A", "something/directory_B", False
        )
        test_config = config.Config(args_object_default)

        # when:
        actual = test_config.isbadpath()

        # then assert:
        mock_print.assert_called_once_with(
            f"\nSTOP... '{test_config.destination_path}' is not a dir\n"
        )
        assert actual is True

    def test_isbadpath_false(self, mock_os, mock_print):
        """should return false if both paths are valid"""

        # given
        mock_os.path.isdir.side_effect = [True, True]
        args_object_default = FakeParseArgs(
            "something/directory_A", "something/directory_B", False
        )
        test_config = config.Config(args_object_default)

        # when:
        actual = test_config.isbadpath()

        # then assert:
        mock_print.assert_not_called()
        assert actual is False
