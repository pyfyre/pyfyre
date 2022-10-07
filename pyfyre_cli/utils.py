import os
import shutil
from typing import Iterator
from contextlib import contextmanager


@contextmanager
def in_path(path: str) -> Iterator[str]:
	original_path = os.getcwd()
	
	try:
		abspath = os.path.abspath(path)
		os.chdir(abspath)
		yield abspath
	finally:
		os.chdir(original_path)


def empty_directory(path: str) -> None:
	for f in os.listdir(path):
		p = os.path.join(path, f)
		
		try:
			shutil.rmtree(p)
		except NotADirectoryError:
			os.remove(p)
