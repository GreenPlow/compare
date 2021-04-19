import pytest
import unittest.mock as mock

from compare import config

# from compare.config import Config


class FakeParseArgs:
    """Example of an object returned from args_helper.parse_args"""

    __test__ = False  # Stops pytest from warning that it cannot instantiate this class

    def __init__(self, origin, destination, hidden):
        self.origin = origin
        self.destination = destination
        self.hidden = hidden


class TestClass:
    def test_call_samepath(self, mocker):
        """should call the samepath method and continue if samepath is false"""

        patcher1 = mock.patch.object(config.Config, "issamepath")
        issamepath_patched = patcher1.start()

        # given:
        mock.patch.object(config, "os", autospec=True)
        args_object_default = FakeParseArgs(
            "something/directory_A", "something/directory_B", False
        )

        test_config = config.Config(args_object_default)

        # when:
        test_config.isvalid()

        # then assert:

        assert issamepath_patched.call_count == 1

        # clean up
        patcher1.stop()
