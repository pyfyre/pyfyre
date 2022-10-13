"""
	This module contains the tools for building the app
	for development and production purposes.
	
	The build process includes but not limited to bundling of the files
	inside the `src` directory as a Brython package to make it usable for the web.
	
	All the build files are saved in the `build` directory so you can just
	serve or deploy the `build` directory to the web.
"""

import os
import sys
import shutil
import pathlib
import importlib
import subprocess
from typing import Iterator, List
from contextlib import contextmanager
try:
	sys.path.append(os.getcwd())
	import settings
except ModuleNotFoundError:
	print("This directory is not a PyFyre project.")
	exit()

_HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
	<head>
		<title>{title}</title>
		
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=yes" />
		
		<link rel="icon" href="{icon}" />
		
		<!-- Start of Brython -->
		<script src="https://cdnjs.cloudflare.com/ajax/libs/brython/3.10.7/brython.min.js"></script>
		<script src="/src.brython.js"></script>
		<script type="text/python">
			import pyfyre
			pyfyre.PRODUCTION = {prod_env}
			import index
		</script>
		<!-- End of Brython -->
		
		{head}
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


def _generate_page_head(*, production: bool) -> List[str]:
	head: List[str] = []
	
	if production:
		head.append('<script src="/modules.brython.js"></script>')
	else:
		head.append(
			'<script src="https://cdnjs.cloudflare.com/ajax/libs/brython/'
			'3.10.7/brython_stdlib.min.js"></script>'
		)
	
	if settings.DEPENDENCIES:
		head.append('<script src="/cpython_packages.brython.js"></script>')
	
	return head


def create_pages(*, production: bool) -> None:
	importlib.reload(settings)
	
	for route, data in settings.ROUTES.items():
		directory = os.path.join(
			"build" if production else "_pyfyre",
			*route.split("/")
		)
		pathlib.Path(directory).mkdir(parents=True, exist_ok=True)
		
		with open(os.path.join(directory, "index.html"), "w") as file:
			head = _generate_page_head(production=production)
			html = _HTML_TEMPLATE.format(
				prod_env=production,
				title=data.get("title", "A PyFyre App"),
				icon=data.get("icon", ""),
				head="\n\t\t".join(head + data.get("head", []))
			)
			file.write(html)


def _cherry_pick_modules(*, production: bool) -> None:
	shutil.copy(
		os.path.join(os.path.dirname(__file__), "brython", "brython_stdlib.js"),
		"__temp__"
	)
	
	with in_path("__temp__"):
		if production:
			copy_to = os.path.join("..", "build")
		else:
			copy_to = os.path.join("..", "_pyfyre")
		
		# This command will detect the only Python modules that are used
		# in the project and will generate a cherry-picked standard libraries
		# for the project to run instead of using bloated `brython_stdlib.js`
		subprocess.run(["brython-cli", "make_modules"])
		os.rename("brython_modules.js", "modules.brython.js")
		shutil.copy("modules.brython.js", copy_to)
		
		# Remove all files and folders except `index.py` to avoid duplicate VFS
		for file in os.listdir():
			if file == "index.py":
				continue
			
			try:
				os.remove(file)
			except IsADirectoryError:
				shutil.rmtree(file)


def bundle_scripts(*, production: bool) -> None:
	try:
		shutil.copytree("src", "__temp__")
	except FileExistsError:
		shutil.rmtree("__temp__")
		shutil.copytree("src", "__temp__")
	
	with open("settings.py") as fn:
		settings = fn.read()
		
		with open(os.path.join("__temp__", "settings.py"), "w") as file:
			file.write(settings)
	
	if production:
		subprocess.run([
			"pyminify", "__temp__",
			"--in-place", "--remove-literal-statements"
		])
		
		subprocess.run([
			"autoflake", "__temp__", "-r", "--in-place", "--quiet",
			"--remove-unused-variables", "--remove-all-unused-imports",
			"--remove-duplicate-keys"
		])
		
		_cherry_pick_modules(production=production)
	
	with in_path("__temp__"):
		if production:
			copy_to = os.path.join("..", "build")
		else:
			copy_to = os.path.join("..", "_pyfyre")
		
		subprocess.run(["brython-cli", "make_package", "src"])
		shutil.copy("src.brython.js", copy_to)
	
	shutil.rmtree("__temp__")


def add_cpython_packages(*, production: bool) -> None:
	importlib.reload(settings)
	
	for package_name in settings.DEPENDENCIES:
		subprocess.run(["brython-cli", "add_package", package_name])
	
	packages_dir = os.path.join("Lib", "site-packages")
	
	if not os.path.isdir(packages_dir):
		return
	
	with in_path(packages_dir):
		if production:
			copy_to = os.path.join("..", "..", "build")
		else:
			copy_to = os.path.join("..", "..", "_pyfyre")
		
		subprocess.run(["brython-cli", "make_package", "cpython_packages"])
		shutil.copy("cpython_packages.brython.js", copy_to)
	
	shutil.rmtree("Lib")


def copy_public_folder(*, production: bool) -> None:
	try:
		if production:
			shutil.copytree("public", "build")
		else:
			shutil.copytree("public", "_pyfyre")
	except FileExistsError:
		if production:
			shutil.rmtree("build")
		else:
			shutil.rmtree("_pyfyre")
		
		copy_public_folder(production=production)


def build_app(*, production: bool = False) -> None:
	if production:
		print("Building app...")
	
	copy_public_folder(production=production)
	create_pages(production=production)
	bundle_scripts(production=production)
	add_cpython_packages(production=production)
	
	if production:
		print("App successfully built.")
