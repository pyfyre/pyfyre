import os
import sys
import shutil
from typing import Iterator
from contextlib import contextmanager


@contextmanager
def in_path(path: str, *, append_to_sys_path: bool = False) -> Iterator[str]:
    original_path = os.getcwd()
    abspath = os.path.abspath(path)

    try:
        if append_to_sys_path:
            sys.path.append(abspath)

        os.chdir(abspath)
        yield abspath
    finally:
        if append_to_sys_path:
            sys.path.remove(abspath)

        os.chdir(original_path)


def empty_directory(path: str) -> None:
    for f in os.listdir(path):
        p = os.path.join(path, f)

        try:
            shutil.rmtree(p)
        except NotADirectoryError:
            os.remove(p)
