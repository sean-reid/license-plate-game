"""Dictionary path helper class."""

from dataclasses import dataclass
from functools import cached_property
from pathlib import Path

from lp_defaults import WORD_DATA_DIR
from lp_repo import REPO_ROOT


@dataclass(frozen=True)
class Dictionary:
    name: str

    @cached_property
    def path(self) -> Path:
        return REPO_ROOT / WORD_DATA_DIR / f"{self.name}.txt"

    @cached_property
    def words(self) -> list[str]:
        with self.path.open() as word_file:
            return word_file.read().lower().splitlines()

    @cached_property
    def word_count(self) -> int:
        return len(self.words)
