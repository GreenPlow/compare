from compare import args_helper


def test_setup_parser_description(mocker):
    """should call the specific argparse method to setup the parser"""
    mocked_argparse = mocker.patch.object(args_helper, "argparse", autospec=True)

    # given:
    test_args = ["something/directory_A", "something/directory_B", "--hidden"]

    # when:
    args_helper.parse_args(test_args)

    # then assert:
    mocked_argparse.ArgumentParser.assert_called_once_with(
        description="copy files from origin to destination dir, while checking for like files."
    )


def test_add_parser_arguments(mocker):
    """should add the required arguments to the parser"""
    mocked_parser = mocker.patch.object(args_helper, "argparse", autospec=True)

    # given:
    test_args = ["something/directory_A", "something/directory_B", "--hidden"]
    parser = mocked_parser.ArgumentParser.return_value

    expected_add_argument_calls = [
        mocker.call("origin", type=str, help="the dir to copy files from"),
        mocker.call(
            "destination",
            type=str,
            help="the dir where files are checked for duplicates and copied to",
        ),
        mocker.call(
            "--hidden",
            action="store_true",
            help="copy hidden files also",
            default=False,
        ),
    ]

    # when:
    args_helper.parse_args(test_args)

    # then assert:
    assert parser.add_argument.call_args_list == expected_add_argument_calls


def test_parse_two_dir_paths():
    """should return object with src, dir, and hidden=False
    program name must be stripped in main.py with args_helper.parse_args([1:])
    """
    # given:
    test_args = ["something/directory_A", "something/directory_B"]

    # when:
    actual = args_helper.parse_args(test_args)

    # then assert:
    assert actual.origin == test_args[0]
    assert actual.destination == test_args[1]
    assert actual.hidden is False


def test_parse_two_dir_paths_with_optional_arg():
    """should return object with src, dir, and hidden=True"""
    # given:
    test_args = ["something/directory_A", "something/directory_B", "--hidden"]

    # when:
    actual = args_helper.parse_args(test_args)

    # then assert:
    assert actual.origin == test_args[0]
    assert actual.destination == test_args[1]
    assert actual.hidden is True
