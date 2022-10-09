"""
	This module creates a PyFyre project in the `__dev__` directory.
	This starts a live server hosting the `__dev__/public` directory.
	The live server watches for changes in the
	`pyfyre` and `pyfyre_cli` directories.
	When the live server detects changes, it will recreate the `__dev__` app.
	
	This is useful to quickly test your changes while developing this project
	on your local environment.
"""

import os
import sys
import importlib
from livereload import Server
from pyfyre_cli.utils import in_path
from pyfyre_cli.create_app import create_app


def _create_app() -> None:
	create_app("__dev__", os.getcwd(), dev_mode=True)
	
	with in_path("__dev__"):
		from pyfyre_cli import build_app
		importlib.reload(build_app)
		build_app.build_app()


if __name__ == "__main__":
	if os.path.dirname(__file__) == os.getcwd():
		sys.path.append(os.path.join(os.getcwd(), "__dev__"))
		_create_app()
		
		server = Server()
		server.watch("pyfyre/", _create_app)
		server.watch("pyfyre_cli/", _create_app)
		server.serve(
			port=8080, host="localhost",
			root=os.path.join("__dev__", "public")
		)
	else:
		print(
			"You must be in the directory of pyfyre to run the development server."
		)
