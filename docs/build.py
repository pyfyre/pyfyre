import os
import subprocess


def export_pyfyre_path() -> str:
    MODULESPATH = os.path.abspath(os.path.join("..", "pyfyre_cli", "copybin"))
    SETTINGSPATH = os.path.abspath(os.path.join("..", "pyfyre_cli", "user"))
    PYTHONPATH = os.getenv("PYTHONPATH") or ""
    return f"export PYTHONPATH={MODULESPATH}:{SETTINGSPATH}:{PYTHONPATH}"


if __name__ == "__main__":
    if os.path.dirname(__file__) == os.getcwd():
        subprocess.run(
            "pip install -r requirements.txt && "
            f"{export_pyfyre_path()} && "
            "make html",
            shell=True,
        )
    else:
        print("You must be in the directory of pyfyre/docs to run this script.")
