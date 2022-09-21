"""
Entry point for pyfyre installed via pip or setuptools.

Example:
```bash
pyfyre create-app hello-world
```
"""

import os
import sys
from contextlib import contextmanager
from typing import List, Optional, Iterator


@contextmanager
def in_directory(directory: str) -> Iterator[str]:
	original_directory = os.getcwd()
	
	try:
		abspath = os.path.abspath(directory)
		os.chdir(abspath)
		yield abspath
	finally:
		os.chdir(original_directory)


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
		print("create-app")
	elif command == "start":
		print("start")
	elif command == "build":
		print("build")
	else:
		with in_directory(os.path.dirname(__file__)):
			with open("outputs/help.txt") as file:
				print(file.read())
