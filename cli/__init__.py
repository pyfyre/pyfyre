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
from cli.utils import in_path
from typing import List, Optional
from cli.create_app import create_app


def execute(args: Optional[List[str]] = None) -> None:
	args = args or sys.argv
	args_list: List[Optional[str]] = [None, None, None]
	
	for index, arg in enumerate(args):
		try:
			args_list[index] = arg
		except IndexError:
			break
	
	command = args_list[1] or "help"
	
	if command == "create-app":
		app_name = args_list[2] or "pyfyre-app"
		app_path = pathlib.Path(os.path.abspath(app_name))
		create_app(
			app_path.parts[-1],
			os.path.join(*app_path.parts[:-1])
		)
	else:
		with in_path(os.path.dirname(__file__)):
			with open("outputs/help.txt") as file:
				print(file.read())
