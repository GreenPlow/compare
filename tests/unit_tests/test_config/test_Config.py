from compare.config import Config
import pytest


class TestParseArgs:
    """Example of an object returned from args_helper.parse_args"""

    __test__ = False  # Stops pytest from warning that it cannot instantiate this class

    def __init__(self, origin, destination, hidden):
        self.origin = origin
        self.destination = destination
        self.hidden = hidden


test_args_object_default = TestParseArgs(
    "something/directory_A", "something/directory_B", False
)

test_args_object_hidden_files = TestParseArgs(
    "something/directory_A", "something/directory_B", True
)


@pytest.mark.parametrize(
    "test_input", [test_args_object_default, test_args_object_hidden_files]
)
def test_create_Config_instance(test_input, mocker):
    """should create a new instance of Config when provided arguments"""
    # given:

    # when:
    config = Config(test_input)

    # then assert:
    assert type(config.origin_path) is str
    assert config.origin_path == test_input.origin

    assert type(config.destination_path) is str
    assert config.destination_path == test_input.destination

    assert type(config.include_hidden) is bool
    assert config.include_hidden == test_input.hidden
