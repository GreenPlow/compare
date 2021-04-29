import pytest
from compare import config


@pytest.fixture
def mock_print(mocker):
    return mocker.patch.object(config, "print")

@pytest.fixture
def mock_os(mocker):
    return mocker.patch.object(config, "os", autospec=True)
