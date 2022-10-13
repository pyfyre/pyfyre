"""
	This script builds the app in the `_pyfyre` directory and starts a
	live server hosting that directory.
	The live server watches for changes in the `public` and `src` directories
	and `settings.py` file.
	When the live server detects changes, it will rebuild the app.
"""

from livereload import Server
from pyfyre_cli.build_app import build_app, bundle_scripts


def run_app() -> None:
	build_app()
	server = Server()
	server.watch("public/", build_app)
	server.watch("src/", lambda: bundle_scripts(production=False))
	server.watch("settings.py", build_app)
	server.serve(root="_pyfyre")
