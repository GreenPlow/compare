from compare.config import Config
import pytest


class TestParseArgs:
    """Example of an object returned from args_helper.parse_args"""

    __test__ = False  # Stops pytest from warning that it cannot instantiate this class

    def __init__(self, origin, destination, hidden):
        self.origin = origin
        self.destination = destination
        self.hidden = hidden


@pytest.fixture()
def fixture_Config(mocker):
    return mocker.patch.object(Config, "Config", autospec=True)


test_args_object_default = TestParseArgs(
    "something/directory_A", "something/directory_B", False
)

test_args_object_hidden_files = TestParseArgs(
    "something/directory_A", "something/directory_B", True
)


@pytest.mark.parametrize(
    "test_input", [test_args_object_default, test_args_object_hidden_files]
)
def test_call_samepath(test_input, mocker):
    """should call the samepath method and continue if samepath is false"""
    # given:
    config = Config(test_input)

    # when:

    # then assert:

    """should call the samepath method and return false if samepath is true"""
