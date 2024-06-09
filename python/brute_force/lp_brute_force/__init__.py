"""Brute force solution to the license plate game."""

from dataclasses import dataclass

from lp_solution import Solution


@dataclass
class BruteForceSolution(Solution):
    def evaluate(self, letters: str) -> str | None:
        shortest_word: str | None = None
        shortest_word_len: int = 100
        for word in self.dictionary.words:
            if len(word) < 3:
                continue
            contains_all_letters: bool = True
            letters_in_order: bool = True
            last_index: int = 0
            word_copy: str = word
            for letter in letters:
                if letter in word_copy:
                    if last_index > word_copy.index(letter):
                        letters_in_order = False
                        break
                    last_index = word_copy.index(letter)
                    word_copy = word_copy.replace(letter, "", 1)
                else:
                    contains_all_letters = False
                    break
            if contains_all_letters and letters_in_order:
                if len(word) < shortest_word_len:
                    shortest_word = word
                    shortest_word_len = len(word)
        return shortest_word
