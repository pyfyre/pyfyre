"""
	This script builds the app and starts a
	live server hosting the `public` directory.
	The live server watches for changes in the `src` directory
	and `settings.py` file.
	When the live server detects changes, it will rebuild the app.
"""

import os
from livereload import Server
from build import build_app, create_pages, bundle_scripts


def build_src() -> None:
	bundle_scripts()


def build_settings() -> None:
	create_pages()
	bundle_scripts()


if __name__ == "__main__":
	if os.path.dirname(__file__) == os.getcwd():
		build_app()
		server = Server()
		server.watch("src/", build_src)
		server.watch("settings.py", build_settings)
		server.serve(root="public")
	else:
		print("You must be in the directory of the project to run it.")
