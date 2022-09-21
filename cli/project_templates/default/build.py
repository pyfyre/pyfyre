import os
import errno
import shutil
from typing import Any


def _print(verbose: bool, *args: Any, **kwargs: Any) -> None:
	if verbose:
		print(*args, **kwargs)


def build_app(verbose: bool = True) -> None:
	_print(verbose, "Building app...")
	scripts_dir = os.path.join("public", "scripts")
	
	if os.path.isdir(scripts_dir):
		shutil.rmtree(scripts_dir)
	
	os.makedirs(scripts_dir)
	
	for f in os.listdir("src"):
		p = os.path.join("src", f)
		
		try:
			shutil.copytree(p, os.path.join(scripts_dir, f))
		except OSError as exc:
			if exc.errno in (errno.ENOTDIR, errno.EINVAL):
				shutil.copy(p, os.path.join(scripts_dir, f))
			else:
				raise
	
	_print(verbose, "App successfully built.")


if __name__ == "__main__":
	build_app()
