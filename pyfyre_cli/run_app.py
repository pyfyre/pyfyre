"""
	This script builds the app in the `_pyfyre` directory and starts a
	live server hosting that directory.
	The live server watches for changes in the `public` and `src` directories,
	as well as the `settings.py` and `template.html` files.
	When the live server detects changes, it will rebuild the app.
"""

from livereload import Server
from pyfyre_cli.build_app import build_app, bundle_scripts, create_pages


def run_app() -> None:
	build_app()
	server = Server()
	server.watch("public/", build_app)
	server.watch("src/", lambda: bundle_scripts(production=False))
	server.watch("settings.py", build_app)
	server.watch("template.html", lambda: create_pages(production=False))
	server.serve(root="_pyfyre")
