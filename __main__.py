"""
Invokes PyFyre when PyFyre module is run as a script.

Example: pyfyre create-app hello-world
"""

import sys

if __name__ == '__main__':
    try:
        from .pyfyre import management
    except ImportError:
        raise ImportError(
            """
            ERR! Cannot find PyFyre. Aborting...
            """
        )

    management.execute_from_command_line(sys.argv)