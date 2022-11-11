"""Run this script before a release.

Read this for more information about making a release:
    https://discord.com/channels/963120162041651281/1021948524390273024/1038051906074988597
"""

import os
import subprocess

if __name__ == "__main__":
    if os.path.dirname(os.path.abspath(__file__)) == os.getcwd():
        SETTINGSPATH = os.path.abspath(os.path.join("pyfyre_cli", "user"))
        PYTHONPATH = os.getenv("PYTHONPATH") or ""

        subprocess.run(
            "black . && mypy . && pip install -e . && "
            f"export PYTHONPATH={SETTINGSPATH}:{PYTHONPATH} && "
            "sphinx-apidoc -M -f -o docs/source pyfyre && "
            "cd docs && make clean html && make html",
            shell=True,
        )
    else:
        print("You must be in the directory of pyfyre to run this script.")
