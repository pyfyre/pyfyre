"""
Entry point for pyfyre installed via pip or setuptools.

Example:
```bash
pyfyre create-app hello-world
```
"""

import os
import sys
import pathlib
from typing import List, Optional
from pyfyre_cli.create_app import create_app
from pyfyre_cli.run_app import run_app

from packages.pyfyre_cli.build_app import build_app

_HELP_MESSAGE = (
	"Manage your PyFyre projects.\n"
	"\n"
	"  Common Commands:\n"
	"    pyfyre help\n"
	"      Show this message.\n"
	"\n"
	"    pyfyre create [name]\n"
	"      Create a new PyFyre project in your current directory.\n"
	"\n"
	"    pyfyre run\n"
	"      Runs the PyFyre project in the current directory.\n"
	"\n"
	"    pyfyre build\n"
	"      Builds the PyFyre project in the current directory for production.\n"
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
		app_name = args_list[2] or "pyfyre-app"
		app_path = pathlib.Path(os.path.abspath(app_name))
		create_app(
			app_path.parts[-1],
			os.path.join(*app_path.parts[:-1])
		)
	elif command == "run":
		run_app()
	elif command == "build":
		build_app(True)
	else:
		print(_HELP_MESSAGE)
