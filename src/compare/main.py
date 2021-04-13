import sys
from compare import args_helper
from compare.config import Config


def main():

    if sys.version_info.major < 3:
        raise ValueError("Python 3 or higher is required.")

    args_obj = args_helper.parse_args(sys.argv[1:])
    config = Config(args_obj)
    if not config.isvalid():
        sys.exit(1)


if __name__ == "__main__":
    main()
