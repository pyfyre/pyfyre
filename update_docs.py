"""Run this script to update the Sphinx generated documentation in the `docs` directory."""

import os
import subprocess

if __name__ == "__main__":
    if os.path.dirname(__file__) == os.getcwd():
        MODULESPATH = os.path.abspath(os.path.join("pyfyre_cli", "copybin"))
        SETTINGSPATH = os.path.abspath(os.path.join("pyfyre_cli", "user"))
        PYTHONPATH = os.getenv("PYTHONPATH") or ""

        subprocess.run(
            "pip install -e . && "
            f"export PYTHONPATH={MODULESPATH}:{SETTINGSPATH}:{PYTHONPATH} && "
            "sphinx-apidoc -f -o docs/source pyfyre && "
            "cd docs && make clean html && make html",
            shell=True,
        )
    else:
        print("You must be in the directory of pyfyre to run this script.")
