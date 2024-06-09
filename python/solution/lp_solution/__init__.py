"""A solution to the license plate game."""

import logging
from dataclasses import dataclass
from logging import RootLogger

from lp_dictionary import Dictionary
from lp_solution_name import SolutionName
from lp_tests import Test

LOGGER: RootLogger = logging.getLogger()


@dataclass
class Solution:
    name: SolutionName
    dictionary: Dictionary

    def evaluate(self, letters: str) -> str:
        raise NotImplementedError

    def run(self, test: Test) -> None:
        for letters in test.tests:
            word: str | None = self.evaluate(letters)
            if word is None:
                LOGGER.info(
                    "Solution %s: there is no word containing the letters %s in order.",
                    self.name.name,
                    letters.upper(),
                )
            else:
                LOGGER.info(
                    "Solution %s: the shortest word containing the letters %s in order is %s.",
                    self.name.name,
                    letters.upper(),
                    word,
                )
