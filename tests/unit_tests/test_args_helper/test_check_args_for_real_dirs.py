import args_helper
import pytest


@pytest.fixture
def mock_print(mocker):
    return mocker.patch.object(args_helper, "print")


# @pytest.fixture
# def mock_path(mocker):
#     return mocker.patch.object(args_helper, 'path', autospec=True)


class TestParseArgs:
    def __init__(self, src, dest, hidden):
        self.src = src
        self.dest = dest
        self.hidden = hidden


test_args_object_default = TestParseArgs(
    "something/directory_A", "something/directory_B", False
)
test_args_object_hidden_files = TestParseArgs(
    "something/directory_A", "something/directory_B", True
)


@pytest.mark.parametrize(
    "test_input", [test_args_object_default, test_args_object_hidden_files]
)
def test_check_two_good_dir_paths(test_input, mocker, mock_print):
    """should print message for good paths"""
    # given:
    expected_print_calls = [
        mocker.call("\nboth paths okay!"),
    ]

    mocker.patch("os.path.isdir", return_value=True)

    # when:
    args_helper.check_args_for_real_dirs(test_input)

    # then:
    assert mock_print.call_args_list == expected_print_calls


def test_check_two_good_dir_pathsh(mocker, mock_print):
    """should print message for good paths"""
    # given:
    test_args_object = TestParseArgs(
        "something/directory_A", "something/directory_B", True
    )

    expected_print_calls = [
        mocker.call("\nboth paths okay!"),
    ]

    mocker.patch("os.path.isdir", return_value=True)

    # when:
    args_helper.check_args_for_real_dirs(test_args_object)

    # then:
    assert mock_print.call_args_list == expected_print_calls


def test_check_two_bad_dir_paths(mocker, mock_print):
    """should print message for bad path on first path to fail"""
    # given:
    test_args_object = TestParseArgs(
        "something/bad/directory_A", "something/bad/directory_B", True
    )

    placeholder = "src"

    expected_isdir_calls = [mocker.call(test_args_object.src)]
    # TODO investigate a method to return the attribute name
    expected_print_calls = [
        mocker.call(
            f"STOP... this is not a dir, {placeholder}: '{test_args_object.src}'"
        ),
    ]

    mock_os_path_isdir = mocker.patch("os.path.isdir", return_value=False)

    # when:
    with pytest.raises(SystemExit, match="1") as excinfo:
        args_helper.check_args_for_real_dirs(test_args_object)

    # then:
    # TODO investigate namespace for mocker and why this works but using from os import path did not work
    assert mock_os_path_isdir.call_args_list == expected_isdir_calls
    assert mock_print.call_args_list == expected_print_calls
    assert excinfo.value.code == 1
