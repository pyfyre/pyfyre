"""
	This module creates a PyFyre project in the `__dev__` directory.
	This starts a live server hosting the `__dev__/public` directory.
	The live server watches for changes in the `pyfyre` and `cli` directories
	and `settings.py` file.
	When the live server detects changes, it will recreate the `__dev__` app.
	
	This is useful to quickly test your changes while developing this project
	on your local environment.
	
	Related Files/Folders:
		- __dev__
		- settings.py
"""

import os
from cli.utils import in_path
from livereload import Server
from cli.create_app import create_app


def _create_app() -> None:
	create_app("__dev__", os.getcwd(), dev_mode=True)
	
	from __dev__.build import build_app
	with in_path("__dev__"):
		build_app()


if __name__ == "__main__":
	if os.path.dirname(__file__) == os.getcwd():
		_create_app()
		
		server = Server()
		server.watch("cli/", _create_app)
		server.watch("pyfyre/", _create_app)
		server.watch("settings.py", _create_app)
		server.serve(root=os.path.join("__dev__", "public"))
	else:
		print(
			"You must be in the directory of pyfyre to run the development server."
		)
