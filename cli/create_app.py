import os
import errno
import shutil
from cli.utils import in_path, empty_directory


def copy_project_template(
	project_path: str, template_name: str = "default"
) -> None:
	with in_path(os.path.dirname(__file__)) as path:
		template_source = os.path.join(path, "project_templates", template_name)
		
		for f in os.listdir(template_source):
			p = os.path.join(template_source, f)
			
			try:
				shutil.copytree(p, os.path.join(project_path, f))
			except OSError as exc:
				if exc.errno in (errno.ENOTDIR, errno.EINVAL):
					shutil.copy(p, project_path)
				else:
					raise


def create_app(app_name: str, app_dir: str) -> None:
	print(f"Creating your PyFyre project '{app_name}'...")
	
	project_path = os.path.join(app_dir, app_name)
	
	if os.path.isdir(project_path):
		prompt = input(
			f"Project '{app_name}' already exists. Want to overwrite "
			f"the directory? (y or n): "
		).lower()
		
		if prompt == "y":
			empty_directory(project_path)
		else:
			print("Aborting...")
			return
	
	copy_project_template(project_path)
	
	
	# # edit the `index.html` file
	# with open(os.path.join(user_dir, "index.html")) as file:
	# 	content = file.read().format(app_name=app_name, app_description=app_description, main_key="{main_key}")
	# with open(os.path.join(path, "public", "index.html"), "w") as file:
	# 	file.write(content)
	
	# # edit the `README.md` file
	# with open(os.path.join(user_dir, "README.md")) as file:
	# 	content = file.read().format(app_name=app_name, app_description=app_description)
	# with open(os.path.join(path, "README.md"), "w") as file:
	# 	file.write(content)
	
	# # edit the `settings.py` file
	# with open(os.path.join(user_dir, "settings.py")) as file:
	# 	content = file.read().format(app_name=app_name, app_description=app_description)
	# with open(os.path.join(path, "settings.py"), "w") as file:
	# 	file.write(content)

	# # edit the `.gitignore` file
	# with open(os.path.join(path, ".gitignore"), "w") as file:
	# 	file.write(__GITIGNORE__)

	# os.chdir(os.path.join(path, "pyfyre"))

	# os.system("brython-cli --install")

	# # Remove unused files produced by Brython
	# os.remove("demo.html")
	# os.remove("unicode.txt")
	# os.remove("README.txt")
	# os.remove("brython.js")
	# os.remove("index.html")

	# rmtree(os.path.join(path, "pyfyre", "management"))
	# rmtree(os.path.join(path, "pyfyre", "user"))
	# rmtree(os.path.join(path, "pyfyre", "shared"))

	# self.minify_dir(os.path.join(path, "pyfyre"))

	# os.system("brython-cli --make_package pyfyre")
	# os.remove("pyfyre.py")
	# os.system("brython-cli --modules")

	# os.chdir(os.path.join(".."))
	# os.mkdir("pyf_modules")

	# with open(os.path.join(path, "pyfyre", "brython_modules.js")) as file:
	# 	content = file.read()
	# with open(os.path.join("pyf_modules", "builtins.js"), "w") as file:
	# 	file.write(content)
	# with open(os.path.join(path, "pyfyre", "pyfyre.brython.js")) as file:
	# 	content = file.read()
	# with open(os.path.join("pyf_modules", "modules.js"), "w") as file:
	# 	file.write(content)
	
	# rmtree("pyfyre")
	# os.remove("__init__.py")
	# os.remove("index.html")
	# os.remove(os.path.join("styles", "__init__.py"))

	# try: rmtree("__pycache__")
	# except: ...

	# try: rmtree(os.path.join("src", "__pycache__"))
	# except: ...

	# try: rmtree(os.path.join("styles", "__pycache__"))
	# except: ...

	# os.system("cls" if os.name == "nt" else "clear")
	
	print("Project created successfully.")
