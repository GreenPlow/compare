import pytest
from compare import config
from tests.unit_tests.test_config.shared_classes import FakeParseArgs

test_args_object_default = FakeParseArgs(
    "something/directory_A", "something/directory_A", False
)


@pytest.fixture
def mock_issamepath(mocker):
    return mocker.patch.object(config.Config, "issamepath")


@pytest.fixture
def mock_isbadpath(mocker):
    return mocker.patch.object(config.Config, "isbadpath")


@pytest.fixture
def mock_printpaths(mocker):
    return mocker.patch.object(config.Config, "printpaths")


class TestClass:
    def test_isvalid_issamepath_called(self, mock_os, mock_issamepath):
        """should call the issamepath method"""
        # given
        test_config = config.Config(test_args_object_default)

        # when
        test_config.isvalid()

        # then
        assert mock_issamepath.call_count == 1

    def test_isvalid_isbadpath_called(self, mock_os, mock_issamepath, mock_isbadpath):
        """should call the isbadpath method"""
        # given
        mock_issamepath.return_value = False
        test_config = config.Config(test_args_object_default)

        # when
        test_config.isvalid()

        # then
        assert mock_isbadpath.call_count == 1

    def test_isvalid_return_true(
        self, mock_issamepath, mock_isbadpath, mock_printpaths
    ):
        """should printpaths and return true if both checks pass"""
        # given
        mock_issamepath.return_value = False
        mock_isbadpath.return_value = False
        test_config = config.Config(test_args_object_default)

        # when
        actual = test_config.isvalid()

        # then
        assert mock_printpaths.call_count == 1
        assert actual is True

    @pytest.mark.parametrize(
        "test_input_issamepath,test_input_isbadpath", [(True, False), (False, True)]
    )
    def test_isvalid_return_false(
        self,
        test_input_issamepath,
        test_input_isbadpath,
        mock_issamepath,
        mock_isbadpath,
        mock_printpaths,
    ):
        """should return false if either checks fails"""
        # given
        mock_issamepath.return_value = test_input_issamepath
        mock_isbadpath.return_value = test_input_isbadpath
        test_config = config.Config(test_args_object_default)

        # when
        actual = test_config.isvalid()

        # then
        assert mock_printpaths.call_count == 0
        assert actual is False
