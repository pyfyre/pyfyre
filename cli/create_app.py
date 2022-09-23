import os
import errno
import shutil
import subprocess
from cli.utils import in_path, empty_directory


def _copy_project_template(
	project_path: str, template_name: str = "default"
) -> None:
	cli_path = os.path.dirname(__file__)
	
	with in_path(cli_path) as path:
		template_source = os.path.join(path, "project_templates", template_name)
		
		for f in os.listdir(template_source):
			p = os.path.join(template_source, f)
			
			try:
				shutil.copytree(p, os.path.join(project_path, f))
			except NotADirectoryError:
				shutil.copy(p, os.path.join(project_path, f))
			except OSError as exc:
				if exc.errno in (errno.ENOTDIR, errno.EINVAL):
					shutil.copy(p, os.path.join(project_path, f))
				else:
					raise
	
	with in_path(os.path.join(cli_path, "..")) as path:
		shutil.copytree("pyfyre", os.path.join(project_path, "src", "pyfyre"))
		
		with in_path("pyfyre"):
			subprocess.run(["brython-cli", "make_package", "pyfyre"])
			shutil.copy("pyfyre.brython.js", os.path.join(project_path, "public"))
			os.remove("pyfyre.brython.js")


def create_app(app_name: str, app_dir: str, *, dev_mode: bool = False) -> None:
	if not dev_mode:
		print(f"Creating your PyFyre project '{app_name}'...")
	
	project_path = os.path.join(app_dir, app_name)
	
	if os.path.isdir(project_path):
		prompt = "y" if dev_mode else input(
			f"Project '{app_name}' already exists. Want to overwrite "
			f"the directory? (y or n): "
		).lower()
		
		if prompt == "y":
			empty_directory(project_path)
		else:
			print("Aborting...")
			return
	else:
		os.makedirs(project_path)
	
	_copy_project_template(project_path)
	
	if not dev_mode:
		print("Project created successfully.")
