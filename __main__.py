"""
Invokes PyFyre when PyFyre module is run as a script.

Example: pyfyre create-app hello-world
"""

import sys

if __name__ == '__main__':
    try:
        from bin import pyfyre
    except ImportError:
        raise ImportError(
            """
            ERR! Cannot find PyFyre. Aborting...
            """
        )

    pyfyre.main(sys.argv)