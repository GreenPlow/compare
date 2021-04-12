import pytest
from Classes import Validate
from tests.unit_tests.test_classes.validate.shared_fixtures import TestParseArgs


test_args_object_default = TestParseArgs(
    "something/directory_A", "something/directory_B", False
)
test_args_object_hidden_files = TestParseArgs(
    "something/directory_A", "something/directory_B", True
)


@pytest.mark.parametrize(
    "test_input", [test_args_object_default, test_args_object_hidden_files]
)
def test_assign_properties_of_new_instance(test_input):
    """should make a new instance of validate with parameter objects properties assigned to the instances properties"""
    # given:

    # when:
    setup = Validate(test_input)

    # then assert:
    assert setup.origin_path == test_input.origin
    assert setup.destination_path == test_input.destination
    assert setup.include_hidden == test_input.hidden
