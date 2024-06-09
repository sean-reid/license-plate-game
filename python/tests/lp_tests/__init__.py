"""Test case helper class."""

from dataclasses import dataclass
from functools import cached_property
from pathlib import Path

from lp_defaults import TEST_DATA_DIR
from lp_repo import REPO_ROOT


@dataclass(frozen=True)
class Test:
    name: str

    @cached_property
    def path(self) -> Path:
        return REPO_ROOT / TEST_DATA_DIR / f"{self.name}.txt"

    @cached_property
    def tests(self) -> list[str]:
        with self.path.open() as test_file:
            return test_file.read().lower().splitlines()

    @cached_property
    def test_count(self) -> int:
        return len(self.tests)
