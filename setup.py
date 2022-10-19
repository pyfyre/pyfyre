import os
import shutil
from typing import List
from setuptools import setup


def get_readme() -> str:
	with open("README.md") as file:
		return file.read()


def get_package_files(directory: str) -> List[str]:
	paths = []
	
	for (path, directories, filenames) in os.walk(directory):
		for filename in filenames:
			paths.append(os.path.join("..", path, filename))
	
	return paths


packages = ["pyfyre", "pyfyre_cli"]
py_modules = ["browser", "settings"]

for module in py_modules:
	shutil.copy(
		os.path.join(
			os.path.dirname(__file__), "pyfyre_cli", "copybin", f"{module}.py"
		),
		os.path.join(os.path.dirname(__file__))
	)

setup(
	name="pyfyre",
	version="0.6.0",
	description="A fast, declarative, and incrementally adoptable Python web "
	"frontend framework for building reactive web user interfaces.",
	long_description=get_readme(),
	long_description_content_type="text/markdown",
	author="StackSpace",
	author_email="stackspace.ph@gmail.com",
	url="https://pyfyre.netlify.app/",
	download_url="https://pypi.org/project/pyfyre/",
	packages=packages,
	package_data={
		"": sum([get_package_files(directory) for directory in packages], [])
	},
	py_modules=py_modules,
	license="MIT",
	project_urls={
		"Source": "https://github.com/pyfyre/pyfyre",
		"Updates": "https://www.facebook.com/pyfyreframework/",
		"Documentation": "https://pyfyre.netlify.app/docs/"
	},
	entry_points={
		"console_scripts": ["pyfyre = pyfyre_cli:execute"]
	},
	install_requires=[i.strip() for i in open("requirements.txt").readlines()]
)

for module in py_modules:
	os.remove(os.path.join(os.path.dirname(__file__), f"{module}.py"))
