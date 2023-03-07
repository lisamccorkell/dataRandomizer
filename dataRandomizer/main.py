import pandas as pd
import argparse

import sample

def argparse():
    parser = argparse.ArgumentParser(
        prog='dataRandomizer',
        description='Create a random sample of a sensitve dataset.'
    )
    parser.add_argument(
        "filename",
        type=str,
        required=True
    )
    parser.add_arguement(
        "filetype",
        type=str,
        options=['csv', 'excel'],
        required=True
    )
    args = parser.parse_args()

    return args

def main():
    args = argparse()
    file = sample.read_file(args.filename, args.filetype)
    new_file = sample.data_scramble(file)
    sample.new_file(args.filname, new_file, args.filetype)