import os
import subprocess


def export_pyfyre_path() -> str:
    MODULESPATH = os.path.abspath(os.path.join("..", "pyfyre_cli", "copybin"))
    SETTINGSPATH = os.path.abspath(os.path.join("..", "pyfyre_cli", "user"))
    PYTHONPATH = os.getenv("PYTHONPATH") or ""
    return f"export PYTHONPATH={MODULESPATH}:{SETTINGSPATH}:{PYTHONPATH}"


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    subprocess.run(
        f"pip install -r requirements.txt && {export_pyfyre_path()} && make html",
        shell=True,
    )
