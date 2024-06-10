"""Brute force solution to the license plate game."""

from dataclasses import dataclass

from lp_solution import Solution


@dataclass
class BruteForceSolution(Solution):
    def evaluate(self, letters: str) -> str | None:
        shortest_word: str | None = None
        shortest_word_len: int = 100
        for word in self.dictionary.words:
            if self.letters_in_order(letters, word):
                if len(word) < shortest_word_len:
                    shortest_word = word
                    shortest_word_len = len(word)
        return shortest_word

    def letters_in_order(self, letters: str, word: str) -> bool:
        pos: int = 0
        for char in word:
            if char == letters[pos]:
                pos += 1
                if pos == len(letters):
                    return True
        return False
