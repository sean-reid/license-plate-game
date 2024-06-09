"""Run solutions."""

import logging
from dataclasses import dataclass
from datetime import datetime as DateTime
from datetime import timedelta as TimeDelta
from logging import RootLogger

from lp_brute_force import BruteForceSolution
from lp_dictionary import Dictionary
from lp_naive import NaiveSolution
from lp_solution_name import SolutionName
from lp_tests import Test

LOGGER: RootLogger = logging.getLogger()


@dataclass(frozen=True)
class RunResult:
    name: SolutionName
    test: Test
    dictionary: Dictionary
    elapsed_time: TimeDelta

    def show_summary(self) -> None:
        LOGGER.info(
            "Solution %s ran on %s tests in %s seconds, using dictionary %s as a reference",
            self.name.name,
            self.test.test_count,
            self.elapsed_time.total_seconds(),
            self.dictionary.name,
        )


@dataclass(frozen=True)
class Runner:
    name: SolutionName
    test: Test
    dictionary: Dictionary

    def run(self) -> RunResult:
        solution: NaiveSolution | BruteForceSolution
        start_time: DateTime = DateTime.now()
        LOGGER.debug(
            "Starting running solution %s at time %s", self.name.name, start_time
        )
        if self.name == SolutionName.NAIVE:
            solution = NaiveSolution(name=self.name, dictionary=self.dictionary)
        elif self.name == SolutionName.BRUTEFORCE:
            solution = BruteForceSolution(name=self.name, dictionary=self.dictionary)
        else:
            LOGGER.error("Unsupported solution type.")
        solution.run(self.test)
        end_time: DateTime = DateTime.now()
        LOGGER.debug("Ended running solution %s at time %s", self.name.name, start_time)
        elapsed_time: TimeDelta = end_time - start_time
        return RunResult(
            name=self.name,
            test=self.test,
            dictionary=self.dictionary,
            elapsed_time=elapsed_time,
        )
