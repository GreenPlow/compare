from compare import main
import sys
import pytest
from typing import NamedTuple


@pytest.fixture()
def fixture_args_helper(mocker):
    return mocker.patch.object(main, "args_helper", autospec=True)


@pytest.fixture()
def fixture_Config(mocker):
    return mocker.patch.object(main, "Config", autospec=True)


class FakeVersion(NamedTuple):
    major: int


def test_fail_python3_version_check(mocker):
    """should raise an error when main.py is called with a version of python below v3"""
    # given:
    unsupported_python = FakeVersion(2)
    mocker.patch.object(sys, "version_info", unsupported_python)

    # then assert:
    with pytest.raises(ValueError, match="Python 3 or higher is required."):
        # when:
        main.main()


def test_pass_python3_version_check(mocker, fixture_args_helper, fixture_Config):
    """should not raise an error when main.py is called with python3"""
    # given:
    supported_python = FakeVersion(3)
    mocker.patch.object(sys, "version_info", supported_python)

    # when:
    try:
        main.main()
    except Exception as e:
        # then assert:
        assert e is None


def test_create_instance_of_Config(mocker, fixture_args_helper, fixture_Config):
    """should create an instance of Config"""
    # given:
    supported_python = FakeVersion(3)
    mocker.patch.object(sys, "version_info", supported_python)

    args_object = fixture_args_helper.parse_args.return_value
    # when:

    main.main()

    # then assert:
    fixture_Config.assert_called_once_with(args_object)
