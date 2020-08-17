
from compare import main
import sys
import pytest
from typing import NamedTuple


@pytest.fixture(autouse=True)
def mockfix_args_helper(mocker):
    mocker.patch.object(main, 'args_helper', autospec=True)
    return main.args_helper


class FakeVersion(NamedTuple):
    major: int


def test_python_version_error(mocker):
    """should raise an error when main.py is called with a version of python below v3"""
    # given:
    unsupported_python = FakeVersion(2)
    mocker.patch.object(sys, 'version_info', unsupported_python)

    # then assert:
    with pytest.raises(ValueError, match="Python 3 or higher is required."):
        # when:
        main.main()


def test_python_is_version_3(mocker, mockfix_args_helper):
    """should not raise an error when main.py is called with python3"""
    # given:
    mocked_Validate = mocker.patch.object(main, 'Validate', autospec=True)
    supported_python = FakeVersion(3)
    # TODO is this the right sys to mock? should it be sys the prod code?
    mocker.patch.object(sys, 'version_info', supported_python)

    # when:
    try:
        main.main()
    except Exception as e:
        # then assert:
        assert e is None


def test_parse_args(mocker, mockfix_args_helper):
    """should call the parse_args() function from args_helper"""
    # given:
    mocked_Validate = mocker.patch.object(main, 'Validate', autospec=True)

    # when:
    main.main()

    # then assert:
    mockfix_args_helper.parse_args.assert_called_once_with(sys.argv[1:])

    # alternate test assertation
    # expected_calls = [
    #     mocker.call(sys.argv[1:])
    # ]
    # assert mockfix_args_helper.parse_args.call_args_list == expected_calls


def test_create_instance_of_validate_and_validate_input(mocker, mockfix_args_helper):
    """should create an instance of validate and call validate_input()"""
    # given:
    mocked_Validate = mocker.patch.object(main, 'Validate', autospec=True)

    supported_python = FakeVersion(3)
    mocker.patch.object(sys, 'version_info', supported_python)

    args_object = mockfix_args_helper.parse_args.return_value
    setup = mocked_Validate.return_value

    # when:

    main.main()

    # then assert:
    mocked_Validate.assert_called_once_with(args_object)
    setup.validate_input.assert_called_once_with()


def test_exit_if_validate_input_is_false(mocker, mockfix_args_helper):
    """should create an instance of validate and exit if paths are not real dirs"""
    # given:
    mocked_Validate = mocker.patch.object(main, 'Validate', autospec=True)

    supported_python = FakeVersion(3)
    mocker.patch.object(sys, 'version_info', supported_python)

    setup = mocked_Validate.return_value
    setup.validate_input.return_value = False

    #then assert:
    with pytest.raises(SystemExit, match="1"):
        # when:
        main.main()


def test_print_okay_of_validate_input_is_true(mocker):
    """should create an instance of validate and print okay if paths are real dirs"""
    # given:
    mocked_print = mocker.patch.object(main, 'print')
    mocked_Validate = mocker.patch.object(main, 'Validate', autospec=True)

    supported_python = FakeVersion(3)
    mocker.patch.object(sys, 'version_info', supported_python)

    setup = mocked_Validate.return_value
    setup.validate_input.return_value = True

    # when:
    main.main()

    # then assert:
    mocked_print.assert_called_once_with('\nBoth paths okay!\n')
    setup.print_paths.assert_called_once_with()
