
import argparse
# from os import path
import sys
import os


def parse_args(args):
    parser = argparse.ArgumentParser(description='copy files from src to dest dir, while checking for like files.')
    parser.add_argument('src', type=str, help='the dir to copy files from')
    parser.add_argument('dest', type=str, help='the dir where files are checked for duplicates and copied to')
    parser.add_argument('--hidden', action='store_true', help='copy hidden files also', default=False)
    return parser.parse_args(args)


def check_args_for_real_dirs(args):
    for arg in vars(args):
        arg_value = getattr(args, arg)
        if isinstance(arg_value, bool):
            continue
        elif os.path.isdir(arg_value):
            continue
        else:
            print(f'STOP... this is not a dir, {arg}: \'{arg_value}\'')
            sys.exit(1)
    print('\nboth paths okay!')
