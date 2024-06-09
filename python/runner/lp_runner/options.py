"""Options for code runner."""

from __future__ import annotations
from dataclasses import dataclass

from lp_solution_name import SolutionName
from lp_log_level import LogLevel
from lp_dictionary import Dictionary
from lp_tests import Test

@dataclass(frozen=True)
class Options:
    log_level: LogLevel
    name: SolutionName
    test: Test
    dictionary: Dictionary

    @staticmethod
    def from_parsed_arguments(parsed_arguments: ParsedArguments) -> Options:
        debug: bool = parsed_arguments.debug
        quiet: bool = parsed_arguments.quiet
        log_level: LogLevel = (
            LogLevel.DEBUG if debug else LogLevel.NONE if quiet else LogLevel.INFO
        )
        name: SolutionName = (
            SolutionName.NAIVE if parsed_arguments.name == "naive"
            else SolutionName.BRUTEFORCE if parsed_arguments.name == "brute_force"
            else SolutionName.NAIVE
        )
        test: Test = Test(parsed_arguments.test)
        dictionary: Dictionary = Dictionary(parsed_arguments.dictionary)

        return Options(
            log_level=log_level,
            name=name,
            test=test,
            dictionary=dictionary,
        )
