import os
import shutil
import pathlib
import settings
import subprocess
from typing import Dict
from typing import Iterator
from contextlib import contextmanager

_HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
	<head>
		<title>{title}</title>
		
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=yes" />
		
		<!-- Start of Brython -->
		<script src="https://cdnjs.cloudflare.com/ajax/libs/brython/3.10.7/brython.min.js"></script>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/brython/3.10.7/brython_stdlib.min.js"></script>
		<script src="/src.brython.js"></script>
		<script type="text/python">import index</script>
		<!-- End of Brython -->
		
		<link rel="icon" href="/favicon.ico" />
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


def _create_page(route: str, data: Dict[str, str]) -> None:
	directory = os.path.join("public", *route.split("/"))
	pathlib.Path(directory).mkdir(parents=True, exist_ok=True)
	
	with open(os.path.join(directory, "index.html"), "w") as file:
		html = _HTML_TEMPLATE.format(title=data["title"])
		file.write(html)


def _bundle_scripts() -> None:
	with in_path("src"):
		subprocess.run(["brython-cli", "make_package", "src"])
		shutil.copy("src.brython.js", os.path.join("..", "public"))
		os.remove("src.brython.js")


def build_app(production: bool = False) -> None:
	if production:
		print("Building app...")
	
	for route, data in settings.ROUTES.items():
		_create_page(route, data)
	
	_bundle_scripts()
	
	if production:
		print("App successfully built.")


if __name__ == "__main__":
	if os.path.dirname(__file__) == os.getcwd():
		build_app(production=True)
	else:
		print("You must be in the directory of the project to build it.")
