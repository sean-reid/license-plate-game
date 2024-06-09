"""Brute force solution to the license plate game."""

from dataclasses import dataclass

from lp_solution import Solution
from lp_solution_name import SolutionName
from lp_dictionary import Dictionary

@dataclass
class BruteForceSolution(Solution):
    def evaluate(self, letters: str) -> str | None:
        shortest_word: str | None = None
        shortest_word_len: int = 100
        for word in self.dictionary.words:
            if not all(l in word for l in letters):
                continue
            letter_indices = [word.index(l) for l in letters]
            if sorted(letter_indices) == letter_indices:
                if len(word) < shortest_word_len:
                    shortest_word = word
                    shortest_word_len = len(word)
        return shortest_word

