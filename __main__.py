"""
Invokes PyFyre when PyFyre module is run as a script.

Example: pyfyre create-app hello-world
"""

import sys

if __name__ == '__main__':
    try:
        from . import bin
    except ImportError:
        raise ImportError(
            """
            ERR! Cannot find PyFyre. Aborting...
            """
        )

    bin.main(sys.argv)