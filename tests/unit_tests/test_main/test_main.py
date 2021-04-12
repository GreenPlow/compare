from compare import main
import sys
import pytest
from typing import NamedTuple


@pytest.fixture()
def fixture_args_helper(mocker):
    return mocker.patch.object(main, "args_helper", autospec=True)

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
