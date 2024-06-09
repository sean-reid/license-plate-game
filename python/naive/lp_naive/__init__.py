"""Naive solution to the license plate game."""

from dataclasses import dataclass
from itertools import combinations

from lp_solution import Solution


@dataclass
class NaiveSolution(Solution):
    def __post_init__(self):
        self.all_words: dict[str, list[str] | None] = {}
        self.shortest_words: dict[str, str | None] = {}
        self.process_words()

    def evaluate(self, letters: str) -> str | None:
        return self.shortest_words.get(letters, None)

    def process_words(self) -> None:
        for word in self.dictionary.words:
            if len(word) > 2:
                for letters_tuple in combinations(word, 3):
                    letters: str = "".join(letters_tuple)
                    shortest_word: str | None = self.shortest_words.get(letters, None)
                    if shortest_word is None or len(word) < len(shortest_word):
                        self.shortest_words[letters] = word
