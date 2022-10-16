import os
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
