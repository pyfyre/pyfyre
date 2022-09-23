import os
import errno
import shutil
import pathlib
import settings
from typing import Dict

_HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
	<head>
		<title>{title}</title>
		
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=yes" />
		
		<script src="https://cdnjs.cloudflare.com/ajax/libs/brython/3.10.7/brython.min.js"></script>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/brython/3.10.7/brython_stdlib.min.js"></script>
		<script src="/pyfyre.brython.js"></script>
		
		<link rel="icon" href="/favicon.ico" />
	</head>
	<body onload="brython()">
		<script type="text/python" src="/index.py"></script>
	</body>
</html>
"""


def _create_page(route: str, data: Dict[str, str]) -> None:
	directory = os.path.join("public", *route.split("/"))
	pathlib.Path(directory).mkdir(parents=True, exist_ok=True)
	
	with open(os.path.join(directory, "index.html"), "w") as file:
		html = _HTML_TEMPLATE.format(title=data["title"])
		file.write(html)


def build_app(production: bool = False) -> None:
	if production:
		print("Building app...")
	
	for route, data in settings.ROUTES.items():
		_create_page(route, data)
	
	scripts_dir = os.path.join("public")
	
	for f in os.listdir("src"):
		if f == "pyfyre":
			continue
		
		p = os.path.join("src", f)
		
		try:
			shutil.copytree(p, os.path.join(scripts_dir, f))
		except FileExistsError:
			shutil.rmtree(os.path.join(scripts_dir, f))
			shutil.copytree(p, os.path.join(scripts_dir, f))
		except OSError as exc:
			if exc.errno in (errno.ENOTDIR, errno.EINVAL):
				shutil.copy(p, os.path.join(scripts_dir, f))
			else:
				raise
	
	if production:
		print("App successfully built.")


if __name__ == "__main__":
	if os.path.dirname(__file__) == os.getcwd():
		build_app(production=True)
	else:
		print("You must be in the directory of the project to build it.")
