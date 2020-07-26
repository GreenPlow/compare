
import args_helper
import pytest


def test_parse_two_dir_paths():
    """should return object with src, dir, and hidden=False"""
    # given:
    # python program name must be stripped when args_helper.parse_args([1:]) is called from main.py
    test_args = ["something/directory_A", "something/directory_B"]

    # when:
    actual = args_helper.parse_args(test_args)

    # then:
    assert actual.src == test_args[0]
    assert actual.dest == test_args[1]
    assert actual.hidden is False


def test_parse_two_dir_paths_with_optional_arg():
    """should return object with src, dir, and hidden=True"""
    # given:
    test_args = ["something/directory_A", "something/directory_B", "--hidden"]

    # when:
    actual = args_helper.parse_args(test_args)

    # then:
    assert actual.src == test_args[0]
    assert actual.dest == test_args[1]
    assert actual.hidden is True


@pytest.fixture
def mocks_for_arg(mocker):
    mocker.patch.object(args_helper, 'argparse', autospec=True)
    return args_helper.argparse


def test_setup_parser(mocker, mocks_for_arg):
    """should call the specific methods of argparse"""
    # given:
    test_args = ["something/directory_A", "something/directory_B", "--hidden"]
    parser = mocks_for_arg.ArgumentParser.return_value

    expected_add_argument_calls = [
        mocker.call('src', type=str, help='the dir to copy files from'),
        mocker.call('dest', type=str, help='the dir where files will be checked for duplicates and copied to'),
        mocker.call('-hidden', '--hidden', action='store_true', help='copy hidden files also', default=False)
    ]

    # when:
    args_helper.parse_args(test_args)

    # then:
    mocks_for_arg.ArgumentParser.assert_called_once_with(
        description='copy files from src to dest dir, while checking for like files.')
    # parser.add_argument.assert_called_with(add_argument_calls)
    assert parser.add_argument.call_args_list == expected_add_argument_calls

# import sys
# from io import StringIO
# def test_handle_no_args(mocker):

# console output
# usage: main.py [-h] [-hidden] src dest
# main.py: error: the following arguments are required: src, dest

#     """should inform user on stdout when all args missing"""
#     # given:
#     test_args = ['main.py']
#     old = sys.argv
#     sys.argv = test_args
#     fakeOutput = mocker.patch('sys.stdout', new=StringIO())
#     print('hello world')
#
#     # when:
#     args_helper.parse_args(test_args)
#
#     # then:
#
#     assert fakeOutput.getvalue().strip() == 'hello world'
#     sys.argv = old

# def test_handle_no_args(capsys, mocker):
#     """should inform user on stdout when all args missing"""
#     test_args = ['main.py']
#     old = sys.argv
#     sys.argv = test_args
#     mocker.patch.object(sys, 'stdout', new=StringIO())
#
#     # when:
#     with args_helper.parse_args(test_args):
#         out, err = capsys.readouterr()
#
#     sys.argv = old


# def test_handle_only_one_arg():
#     """should inform user on stdout for second required arg"""
#     pass
#
#
# def test_handle_help():
#     """should inform user of help doc for -help/--help arg"""
#     pass






