import pytest
from compare import config
from tests.unit_tests.test_config.shared_classes import FakeParseArgs


class TestClass:

    test_args_object_default = FakeParseArgs(
        "something/directory_A", "something/directory_B", False
    )
    test_args_object_hidden_files = FakeParseArgs(
        "something/directory_A", "something/directory_B", True
    )

    @pytest.mark.parametrize(
        "test_input", [test_args_object_default, test_args_object_hidden_files]
    )
    def test_printpaths(self, mocker, test_input, mock_print):
        """should print both paths"""

        # given:
        test_config = config.Config(test_input)

        # when:
        actual = test_config.printpaths()

        # then assert:
        expected_print_calls = [
            mocker.call("path to copy files from...", test_config.origin_path),
            mocker.call(
                "path to put copied files...", test_config.destination_path, "\n"
            ),
        ]
        assert mock_print.call_args_list == expected_print_calls
