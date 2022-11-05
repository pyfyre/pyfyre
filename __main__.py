"""Entry point for PyFyre CLI.

Example:
    >>> cd /path/to/pyfyre/..
    >>> python pyfyre create hello-world
"""

import sys
import pyfyre_cli

if __name__ == "__main__":
    pyfyre_cli.execute(sys.argv)
