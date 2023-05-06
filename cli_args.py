# Standard Library
from argparse import ArgumentParser, BooleanOptionalAction


def get_args():
    parser = ArgumentParser()
    parser.add_argument("-d", "--debug", action=BooleanOptionalAction)

    return parser.parse_args()
