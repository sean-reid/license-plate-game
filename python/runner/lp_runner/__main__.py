"""Main entrypoint for code runner."""

import sys

from lp_runner.main import main

if __name__ == "__main__":
    main(sys.argv[1:])
