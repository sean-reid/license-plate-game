"""Argument parser for code runner."""

from argparse import Namespace as ParsedArguments, ArgumentParser
from typing import Sequence

def build_argument_parser() -> ArgumentParser:
    parser: ArgumentParser = ArgumentParser(prog="runner")
    
    logging_group = parser.add_mutually_exclusive_group()
    logging_group.add_argument("--debug", action="store_true", help="Print verbose logging")
    logging_group.add_argument("--quiet", action="store_true", help="Print no logging")

    parser.add_argument("--name", default="brute_force", help="Short name of solution to run")
    parser.add_argument("--test", default="combos1", help="Short name of test case set to run")
    parser.add_argument("--dictionary", default="words_alpha", help="Short name of dictionary to reference")

    return parser
