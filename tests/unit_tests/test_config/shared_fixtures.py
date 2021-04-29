import pytest
from compare import config


@pytest.fixture
def mock_print(mocker):
    return mocker.patch.object(config, "print")
