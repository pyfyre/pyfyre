"""
	This script builds the app and starts a
	live server hosting the `public` directory.
	The live server watches for changes in the `src` directory
	and `settings.py` file.
	When the live server detects changes, it will rebuild the app.
"""

from livereload import Server
from pyfyre_cli.build_app import (
	build_app, create_pages, bundle_scripts, add_cpython_packages
)


def _build_src() -> None:
	bundle_scripts(production=False)


def _build_settings() -> None:
	create_pages(production=False)
	bundle_scripts(production=False)
	add_cpython_packages()


def run_app() -> None:
	build_app()
	server = Server()
	server.watch("src/", _build_src)
	server.watch("settings.py", _build_settings)
	server.serve(root="public")
