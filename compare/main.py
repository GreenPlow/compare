
import sys
import args_helper
from Classes import Validate


def main():

    if sys.version_info.major < 3:
        raise ValueError("Python 3 or higher is required.")

    args_obj = args_helper.parse_args(sys.argv[1:])

    setup = Validate(args_obj)
    # TODO handle "" for paths with spaces
    if not setup.validate_input():
        sys.exit(1)
    else:
        print('\nBoth paths okay!\n')
        setup.print_paths()


if __name__ == "__main__":
    main()
