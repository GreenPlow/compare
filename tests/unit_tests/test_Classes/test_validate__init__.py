
import pytest
from Classes import Validate


class TestParseArgs:
    def __init__(self, origin, destination, hidden):
        self.origin = origin
        self.destination = destination
        self.hidden = hidden


test_args_object_default = TestParseArgs('something/directory_A', 'something/directory_B', False)
test_args_object_hidden_files = TestParseArgs('something/directory_A', 'something/directory_B', True)


@pytest.mark.parametrize("test_input", [test_args_object_default, test_args_object_hidden_files])
def test_validate__init__(test_input):
    """should make a new instance of validate"""
    # given:

    # when:
    setup = Validate(test_input)

    # then assert:
    assert setup.origin_path == test_input.origin
    assert setup.destination_path == test_input.destination
    assert setup.include_hidden == test_input.hidden
