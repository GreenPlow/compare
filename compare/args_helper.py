
import argparse


def parse_args(args):
    parser = argparse.ArgumentParser(description='copy files from src to dest dir, while checking for like files.')
    parser.add_argument('src', type=str, help='the dir to copy files from')
    parser.add_argument('dest', type=str, help='the dir where files are checked for duplicates and copied to')
    parser.add_argument('--hidden', action='store_true', help='copy hidden files also', default=False)
    return parser.parse_args(args)
