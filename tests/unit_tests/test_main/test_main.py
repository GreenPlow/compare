
from compare import main
import sys
import pytest
from typing import NamedTuple


@pytest.fixture(autouse=True)
def fixture_args_helper(mocker):
    mocker.patch.object(main, 'args_helper', autospec=True)
    return main.args_helper


class FakeVersion(NamedTuple):
    major: int


def test_fail_python3_version_check(mocker):
    """should raise an error when main.py is called with a version of python below v3"""
    # given:
    unsupported_python = FakeVersion(2)
    mocker.patch.object(sys, 'version_info', unsupported_python)

    # then assert:
    with pytest.raises(ValueError, match="Python 3 or higher is required."):
        # when:
        main.main()


def test_pass_python3_version_check(mocker, fixture_args_helper):
    """should not raise an error when main.py is called with python3"""
    # given:
    mocker.patch.object(main, 'Validate', autospec=True)
    supported_python = FakeVersion(3)
    # TODO review second usage of patch.object(). Should we mock the sys in the prod file?
    mocker.patch.object(sys, 'version_info', supported_python)

    # when:
    try:
        main.main()
    except Exception as e:
        # then assert:
        assert e is None


def test_get_arguments_from_parse_args(mocker, fixture_args_helper):
    """should call the parse_args() function from args_helper with [1:]"""
    # given:
    mocker.patch.object(main, 'Validate', autospec=True)

    # when:
    main.main()

    # then assert:
    fixture_args_helper.parse_args.assert_called_once_with(sys.argv[1:])


def test_create_instance_of_validate_and_validate_input(mocker, fixture_args_helper):
    """should create an instance of validate and call validate_input()"""
    # given:
    validate_mock = mocker.patch.object(main, 'Validate', autospec=True)
    supported_python = FakeVersion(3)
    mocker.patch.object(sys, 'version_info', supported_python)

    args_object = fixture_args_helper.parse_args.return_value
    setup_mock = validate_mock.return_value

    # when:

    main.main()

    # then assert:
    validate_mock.assert_called_once_with(args_object)
    setup_mock.validate_input.assert_called_once_with()


def test_if_validate_input_is_false_exit_script(mocker, fixture_args_helper):
    """should exit if paths are not real dirs"""
    # given:
    validate_mock = mocker.patch.object(main, 'Validate', autospec=True)

    supported_python = FakeVersion(3)
    mocker.patch.object(sys, 'version_info', supported_python)

    setup_mock = validate_mock.return_value
    setup_mock.validate_input.return_value = False

    # then assert:
    with pytest.raises(SystemExit, match="1"):
        # when:
        main.main()


def test_if_validate_input_is_true_print_text(mocker):
    """should print okay and dir paths if paths are real dirs"""
    # given:
    mocked_print = mocker.patch.object(main, 'print')
    validate_mock = mocker.patch.object(main, 'Validate', autospec=True)

    supported_python = FakeVersion(3)
    mocker.patch.object(sys, 'version_info', supported_python)

    setup_mock = validate_mock.return_value
    setup_mock.validate_input.return_value = True

    # when:
    main.main()

    # then assert:
    mocked_print.assert_called_once_with('\nBoth paths okay!\n')
    setup_mock.print_paths.assert_called_once_with()
