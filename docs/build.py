import os
import subprocess

if __name__ == "__main__":
    MODULESPATH = os.path.abspath(os.path.join("..", "pyfyre_cli", "copybin"))
    SETTINGSPATH = os.path.abspath(os.path.join("..", "pyfyre_cli", "user"))
    PYTHONPATH = os.getenv("PYTHONPATH") or ""

    subprocess.run(
        "pip install -r requirements.txt && "
        f"export PYTHONPATH={MODULESPATH}:{SETTINGSPATH}:{PYTHONPATH} && "
        "make html",
        shell=True,
    )
