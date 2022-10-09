"""
Entry point for pyfyre installed via pip or setuptools.

Example:
```bash
pyfyre create hello-world
```
"""

import os
import sys
import pathlib
from typing import List, Optional

_HELP_MESSAGE = (
	"Manage your PyFyre projects.\n"
	"\n"
	"  Common Commands:\n"
	"    pyfyre help\n"
	"      Show this message.\n"
	"\n"
	"    pyfyre create [path]\n"
	"      Create a new PyFyre project in the specified path.\n"
	"      The directory of the path will be your project's name.\n"
	"\n"
	"    pyfyre run\n"
	"      Run the PyFyre project in the current directory in development mode.\n"
	"\n"
	"    pyfyre build\n"
	"      Build the PyFyre project in the current directory for production.\n"
)


def execute(args: Optional[List[str]] = None) -> None:
	args = args or sys.argv
	args_list: List[Optional[str]] = [None, None, None]
	
	for index, arg in enumerate(args):
		try:
			args_list[index] = arg
		except IndexError:
			break
	
	command = args_list[1] or "help"
	
	if command == "create":
		from pyfyre_cli.create_app import create_app
		app_name = args_list[2] or "pyfyre-app"
		app_path = pathlib.Path(os.path.abspath(app_name))
		create_app(
			app_path.parts[-1],
			os.path.join(*app_path.parts[:-1])
		)
	elif command == "run":
		from pyfyre_cli.run_app import run_app
		run_app()
	elif command == "build":
		from pyfyre_cli.build_app import build_app
		build_app(production=True)
	else:
		print(_HELP_MESSAGE)
