"""
Entry point for pyfyre.

Example:
```bash
python pyfyre create-app hello-world
```
"""

import sys
import cli

if __name__ == "__main__":
	cli.execute(sys.argv)
