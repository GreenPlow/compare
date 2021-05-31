from compare import main
import sys
import pytest
from typing import NamedTuple


class FakeVersion(NamedTuple):
    major: int


@pytest.fixture()
def fixture_args_helper(mocker):
    return mocker.patch.object(main, "args_helper", autospec=True)


@pytest.fixture()
def fixture_Config(mocker):
    return mocker.patch.object(main, "Config", autospec=True)


@pytest.fixture()
def fixture_Python3(mocker):
    supported_python = FakeVersion(3)
    mocker.patch.object(sys, "version_info", supported_python)


def test_fail_python3_version_check(mocker):
    """should raise an error when main.py is called with a version of python below v3"""
    # given:
    unsupported_python = FakeVersion(2)
    mocker.patch.object(sys, "version_info", unsupported_python)

    # then assert:
    with pytest.raises(ValueError, match="Python 3 or higher is required."):
        # when:
        main.main()


def test_pass_python3_version_check(
    fixture_Python3, fixture_args_helper, fixture_Config
):
    """should not raise an error when main.py is called with python3"""
    # given:

    # when:
    try:
        main.main()
    except Exception as e:
        # then assert:
        assert e is None


def test_create_instance_of_Config(
    fixture_Python3, fixture_args_helper, fixture_Config
):
    """should create an instance of Config"""
    # given:
    args_object = fixture_args_helper.parse_args.return_value

    # when:
    main.main()

    # then assert:
    fixture_Config.assert_called_once_with(args_object)


def test_isvalid_config(fixture_Python3, fixture_args_helper, fixture_Config):
    """should call isvalid"""
    # given:
    args_object = fixture_args_helper.parse_args.return_value
    config = fixture_Config.return_value

    # when:
    main.main()

    # then assert:
    config.isvalid.assert_called_once_with()


def test_exit_on_failed_validation(
    fixture_Python3, fixture_args_helper, fixture_Config
):
    """should exit if the config validation fails"""
    # given:
    config_mock = fixture_Config.return_value
    config_mock.isvalid.return_value = False

    # then assert:
    with pytest.raises(SystemExit, match="1"):
        # when:
        main.main()


def test_do_not_exit_on_isvalid(fixture_Python3, fixture_args_helper, fixture_Config):
    """should exit if the config validation fails"""
    # given:
    config_mock = fixture_Config.return_value
    config_mock.isvalid.return_value = True

    # when:
    main.main()

    # then assert:
    config_mock.isvalid.assert_called_once_with()
