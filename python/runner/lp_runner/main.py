"""Main function for code runner."""

import logging
from argparse import ArgumentParser
from argparse import Namespace as ParsedArguments
from typing import Sequence

from lp_runner.arguments import build_argument_parser
from lp_runner.options import Options
from lp_runner.runner import Runner, RunResult


def main(args: Sequence[str]):
    parser: ArgumentParser = build_argument_parser()
    parsed_arguments: ParsedArguments = parser.parse_args(args)
    options: Options = Options.from_parsed_arguments(parsed_arguments)

    logging.basicConfig(level=options.log_level.value)

    runner: Runner = Runner(
        options.name,
        options.test,
        options.dictionary,
    )
    run_result: RunResult = runner.run()
    run_result.show_summary()
