"""Repository helper tools."""
import os

from dataclasses import dataclass
from pathlib import Path


@dataclass
class Repo:
    @staticmethod
    def get_repo_root():
        current_dir = Path.cwd()
        while not (current_dir / '.git').exists():
            # Move up one directory
            current_dir = current_dir.parent
            # Check if we reached the root
            if current_dir == Path('/'):
                raise Exception("Not inside a git repository")
        return current_dir

REPO_ROOT: Path = Repo.get_repo_root()
