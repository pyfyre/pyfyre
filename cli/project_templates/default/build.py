"""
	This module contains the tools for building the app
	for development and production purposes.
	For instance, this module will build the app for production
	if it is run directly as a script (not imported).
	
	The build process includes but not limited to bundling of the files
	inside the `src` directory as a Brython package to make it usable for the web.
	
	All the build files are stored in the `public` directory so you can just
	serve or deploy the `public` directory to the web.
"""

import os
import shutil
import pathlib
import settings
import importlib
import subprocess
from typing import Iterator
from contextlib import contextmanager

_HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
	<head>
		<title>{title}</title>
		
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=yes" />
		
		<!-- Start of Brython -->
		<script src="/brython.js"></script>
		<script src="/brython_stdlib.js"></script>
		<script src="/cpython_packages.brython.js"></script>
		<script src="/src.brython.js"></script>
		<script type="text/python">import index</script>
		<!-- End of Brython -->
		
		<link rel="icon" href="{icon}" />
	</head>
	<body onload="brython()"></body>
</html>
"""


@contextmanager
def in_path(path: str) -> Iterator[str]:
	original_path = os.getcwd()
	
	try:
		abspath = os.path.abspath(path)
		os.chdir(abspath)
		yield abspath
	finally:
		os.chdir(original_path)


def create_pages() -> None:
	importlib.reload(settings)
	
	for route, data in settings.ROUTES.items():
		directory = os.path.join("public", *route.split("/"))
		pathlib.Path(directory).mkdir(parents=True, exist_ok=True)
		
		with open(os.path.join(directory, "index.html"), "w") as file:
			html = _HTML_TEMPLATE.format(
				title=data.get("title", "A PyFyre App"),
				icon=data.get("icon", "")
			)
			file.write(html)


def bundle_scripts() -> None:
	with open("settings.py") as fn:
		settings = fn.read()
		
		with in_path("src"):
			with open("settings.py", "w") as file:
				file.write(settings)
			
			subprocess.run(["brython-cli", "make_package", "src"])
			shutil.copy("src.brython.js", os.path.join("..", "public"))
			
			os.remove("src.brython.js")
			os.remove("settings.py")


def add_cpython_packages() -> None:
	importlib.reload(settings)
	
	for package_name in settings.DEPENDENCIES:
		subprocess.run(["brython-cli", "add_package", package_name])
	
	packages_dir = os.path.join("Lib", "site-packages")
	
	if not os.path.isdir(packages_dir):
		return
	
	with in_path(packages_dir):
		subprocess.run(["brython-cli", "make_package", "cpython_packages"])
		shutil.copy(
			"cpython_packages.brython.js",
			os.path.join("..", "..", "public")
		)
	
	shutil.rmtree("Lib")


def build_app(production: bool = False) -> None:
	if production:
		print("Building app...")
	
	create_pages()
	bundle_scripts()
	add_cpython_packages()
	
	if production:
		print("App successfully built.")


if __name__ == "__main__":
	if os.path.dirname(__file__) == os.getcwd():
		build_app(production=True)
	else:
		print("You must be in the directory of the project to build it.")
