"""
	This script builds the app and starts a
	live server hosting the `public` directory.
	The live server watches for changes in the `src` directory
	and `settings.py` file.
	When the live server detects changes, it will rebuild the app.
"""

import os
from build import build_app
from livereload import Server

if __name__ == "__main__":
	if os.path.dirname(__file__) == os.getcwd():
		build_app()
		server = Server()
		server.watch("src/", build_app)
		server.watch("settings.py", build_app)
		server.serve(root="public")
	else:
		print("You must be in the directory of the project to run it.")
