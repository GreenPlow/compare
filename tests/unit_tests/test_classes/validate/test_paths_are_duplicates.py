
import Classes
from Classes import Validate
from tests.unit_tests.test_classes.validate.shared_fixtures import TestParseArgs

test_args_object_default = TestParseArgs('something/directory_A', 'something/directory_B', False)
test_args_object_same = TestParseArgs('something/directory_A', 'something/directory_A', False)


def test_call_os_path_samefile(mocker):
    # given:
    os_mock = mocker.patch.object(Classes, 'os')
    instance = Validate(test_args_object_default)

    # when:
    instance.paths_are_duplicates()

    # then:
    os_mock.path.samefile.assert_called_once_with(instance.origin_path, instance.destination_path)


def test_call_os_path_samefile_true(mocker):
    # given:
    mocker.patch("os.path.samefile", return_value=True)
    print_mock = mocker.patch.object(Classes, 'print')
    instance = Validate(test_args_object_same)

    # when:
    result = instance.paths_are_duplicates()

    # then:
    print_mock.assert_called_once_with("\nSTOP... The origin and destination paths are the same.\n")
    assert result is True


def test_call_os_path_samefile_false(mocker):
    # given:
    mocker.patch("os.path.samefile", return_value=False)
    print_mock = mocker.patch.object(Classes, 'print')
    instance = Validate(test_args_object_default)

    # when:
    result = instance.paths_are_duplicates()

    # then:
    print_mock.assert_not_called()
    assert result is None
