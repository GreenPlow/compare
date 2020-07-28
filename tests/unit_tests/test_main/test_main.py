
from compare import main
import sys
import pytest
from typing import NamedTuple


def test_python_version_error(mocker):
    """raises an error when main.py is called with a version of python below 3"""
    # given:
    class FakeVersion(NamedTuple):
        major: int
    unsupported_python = FakeVersion(2)
    mocker.patch.object(sys, 'version_info', unsupported_python)

    # then:
    with pytest.raises(ValueError, match="Python 3 or higher is required."):
        # when:
        main.main()


def test_python_version_3(mocker):
    """does not raise an error when main.py is called with python3"""
    # given:
    class FakeVersion(NamedTuple):
        major: int
    unsupported_python = FakeVersion(3)
    # TODO is this the right sys to mock? should it be the sys in this file or prod code?
    mocker.patch.object(sys, 'version_info', unsupported_python)

    mocker.patch.object(main, 'args_helper', autospec=True)

    # when:
    actual = main.main()
    expected = None

    # then:
    assert actual == expected, "main does not return anything, main should not raise error for python3"


def test_parse_args(mocker):
    """should call the parse_args() function from args_helper"""
    # given:
    mocked_args_helper = mocker.patch.object(main, 'args_helper', autospec=True)

    # when:
    main.main()

    # then:
    mocked_args_helper.parse_args.assert_called_once_with(sys.argv[1:])


def test_check_paths_are_real(mocker):
    """should call the fn() to check that the paths from args are real dirs"""
    # given:
    mocked_args_helper = mocker.patch.object(main, 'args_helper', autospec=True)
    args_object = mocked_args_helper.parse_args.return_value

    # when:
    main.main()

    # then:
    mocked_args_helper.check_args_for_real_dirs.assert_called_once_with(args_object)
