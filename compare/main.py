
import sys
import args_helper


def main():

    if sys.version_info.major < 3:
        raise ValueError("Python 3 or higher is required.")

    args_object = args_helper.parse_args(sys.argv[1:])
    # TODO handle "" for paths with spaces

    args_helper.check_args_for_real_dirs(args_object)


if __name__ == "__main__":
    main()
