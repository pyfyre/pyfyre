"""
Entry point for pyfyre.

Example:
```bash
python pyfyre create-app hello-world
```
"""

import sys
import pyfyre_cli

if __name__ == "__main__":
	pyfyre_cli.execute(sys.argv)
