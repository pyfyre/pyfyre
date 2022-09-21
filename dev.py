"""
	This module creates a PyFyre project in the `__dev__` directory.
	This is useful to quickly test your changes while developing this project.
"""

import os
from cli.utils import in_path
from cli.create_app import create_app

if __name__ == "__main__":
	cwd = os.path.dirname(os.path.abspath(__file__))
	os.chdir(cwd)
	
	create_app("__dev__", cwd)
	from __dev__.build import build_app
	
	with in_path("__dev__"):
		build_app()
