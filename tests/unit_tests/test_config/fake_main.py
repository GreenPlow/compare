# import pytest
# from unittest import mock
# from main import Config


# class TestParseArgs:

#     #setting up the pactchers for issamepath and isbadpath
#     patcher1 = mock.patch.object(Config, 'issamepath')
#     issamepath_patched = patcher1.start()

#     patcher2 = mock.patch.object(Config, 'isbadpath')
#     isbadpath_patched = patcher2.start()

#     def test_isvalid_issamepath_called(self):

#         config = Config()
#         config.isvalid()

#         # after calling isvalid(), it will call the first if statement
#         # which is issampath()
#         assert self.issamepath_patched.call_count == 1

#     def test_isvalid_isbadpath_called(self):

#         # setting issamepath to false so that isvalid() will enter elif
#         self.issamepath_patched.return_value = False

#         config = Config()
#         config.isvalid()

#         assert self.isbadpath_patched.call_count == 1

#     def test_isvalid_return_true(self):

#         # setting isamepath() and isbadpath() to false, so isvalid() will enter else
#         # and return true
#         self.issamepath_patched.return_value = False
#         self.isbadpath_patched.return_value = False

#         config = Config()

#         assert config.isvalid()

#     def test_isvalid_return_false(self):
#         # TODO
#         pass
