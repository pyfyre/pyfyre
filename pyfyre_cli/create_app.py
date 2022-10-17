import os
import shutil
from pyfyre_cli.utils import in_path, empty_directory


def _copy_project_template(project_path: str) -> None:
	cli_path = os.path.dirname(__file__)
	
	with in_path(cli_path) as path:
		shutil.copytree(os.path.join(path, "user"), project_path, dirs_exist_ok=True)
	
	with in_path(os.path.join(cli_path, "..")):
		shutil.copytree("pyfyre", os.path.join(project_path, "src", "pyfyre"))


def create_app(app_name: str, app_dir: str, *, dev_mode: bool = False) -> None:
	if not dev_mode:
		print(f"Creating your PyFyre project '{app_name}'...")
	
	project_path = os.path.join(app_dir, app_name)
	
	if os.path.isdir(project_path):
		prompt = "y" if dev_mode else input(
			f"Project '{app_name}' already exists.\nWant to overwrite "
			f"the directory? (y or n): "
		).lower()
		
		if prompt == "y":
			empty_directory(project_path)
		else:
			print("Aborting...")
			return
	
	_copy_project_template(project_path)
	
	if not dev_mode:
		print("Project created successfully.")
