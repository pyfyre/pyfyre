"""
This module contains the tools for building the app
for development and production purposes.

The build process includes but not limited to bundling of the files
inside the `src` directory as a Brython package to make it usable for the web.

All the build files are saved in the `build` directory so you can just
serve or deploy the `build` directory to the web.
"""

import os
import sys
import shutil
import pathlib
import warnings
import importlib
import subprocess
from typing import List
from pyfyre_cli.utils import in_path

try:
    sys.path.append(os.getcwd())
    import settings
except ModuleNotFoundError:
    print("This directory is not a PyFyre project.")
    exit()


def _generate_page_head(*, production: bool) -> List[str]:
    head: List[str] = []

    if production:
        head.append('<script src="/modules.brython.js" defer="defer"></script>')
    else:
        head.append(
            '<script src="https://cdnjs.cloudflare.com/ajax/libs/brython/'
            '3.10.7/brython_stdlib.min.js" defer="defer"></script>'
        )

    if settings.PYTHON_DEPENDENCIES:
        head.append(
            '<script src="/cpython_packages.brython.js" defer="defer"></script>'
        )

    return head


def _generate_page_body(route_name: str) -> str:
    shutil.copytree("src", "__temp__", dirs_exist_ok=True)
    shutil.copy("settings.py", "__temp__")

    for module in ["browser", "interpreter", "javascript"]:
        shutil.copy(
            os.path.join(os.path.dirname(__file__), "copybin", f"{module}.py"),
            "__temp__",
        )

    with in_path("__temp__", append_to_sys_path=True):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")

            import pyfyre

            pyfyre.PRODUCTION = True

            import index
            from pyfyre.router import RouteManager

            # Set [parse_route] to `False` because the [get_node] method
            # uses a Brython function which will not work
            # if [parse_route] is `True` in this context because
            # we are running the app using Python and not Brython.
            # Brython functions like [createElement] will not work in this context
            # that's why we would not want to parse the route which uses
            # a Brython function (document.createElement).
            html = RouteManager.get_node(route_name, parse_route=False).html()

    shutil.rmtree("__temp__")
    return html


def create_pages(*, production: bool) -> None:
    importlib.reload(settings)

    with open("template.html") as file:
        html_template = file.read()

    for route, data in settings.ROUTES.items():
        directory = os.path.join(
            "build" if production else "_pyfyre", *route.split("/")
        )
        pathlib.Path(directory).mkdir(parents=True, exist_ok=True)

        with open(os.path.join(directory, "index.html"), "w") as file:
            head = _generate_page_head(production=production)
            html = html_template.format(
                prod_env=production,
                brython_options=str(
                    {
                        "debug": 0 if production else 1,
                        "cache": 1 if production else 0,
                    }
                ),
                title=data.get("title", "A PyFyre App"),
                icon=data.get("icon", ""),
                head="\n\t\t".join(head + data.get("head", [])),
                body=_generate_page_body(route) if production else "",
            )
            file.write(html)


def _cherry_pick_modules() -> None:
    shutil.copy(
        os.path.join(os.path.dirname(__file__), "copybin", "brython_stdlib.js"),
        "__temp__",
    )

    with in_path("__temp__"):
        # This command will detect the only Python modules that are used
        # in the project and will generate a cherry-picked standard libraries
        # for the project to run instead of using bloated `brython_stdlib.js`
        subprocess.run(["brython-cli", "make_modules"])
        os.rename("brython_modules.js", "modules.brython.js")
        shutil.copy("modules.brython.js", os.path.join("..", "build"))

        # Remove all files and folders except `index.py` to avoid duplicate VFS
        for file in os.listdir():
            if file == "index.py":
                continue

            if os.path.isfile(file):
                os.remove(file)
            else:
                shutil.rmtree(file)


def bundle_scripts(*, production: bool) -> None:
    shutil.copytree("src", "__temp__", dirs_exist_ok=True)
    shutil.copy("settings.py", "__temp__")

    temp_dir = os.path.abspath("__temp__")
    with in_path(os.path.join(os.path.dirname(__file__), "..")):
        shutil.copytree("pyfyre", os.path.join(temp_dir, "pyfyre"), dirs_exist_ok=True)

    if production:
        subprocess.run(
            ["pyminify", "__temp__", "--in-place", "--remove-literal-statements"]
        )

        subprocess.run(
            [
                "autoflake",
                "__temp__",
                "-r",
                "--in-place",
                "--quiet",
                "--remove-unused-variables",
                "--remove-all-unused-imports",
                "--remove-duplicate-keys",
            ]
        )

        _cherry_pick_modules()

    with in_path("__temp__"):
        subprocess.run(["brython-cli", "make_package", "src"])
        shutil.copy(
            "src.brython.js", os.path.join("..", "build" if production else "_pyfyre")
        )

    shutil.rmtree("__temp__")


def add_cpython_packages(*, production: bool) -> None:
    importlib.reload(settings)

    for package_name in settings.PYTHON_DEPENDENCIES:
        subprocess.run(["brython-cli", "add_package", package_name])

    packages_dir = os.path.join("Lib", "site-packages")

    if not os.path.isdir(packages_dir):
        return

    with in_path(packages_dir):
        subprocess.run(["brython-cli", "make_package", "cpython_packages"])
        shutil.copy(
            "cpython_packages.brython.js",
            os.path.join("..", "..", "build" if production else "_pyfyre"),
        )

    shutil.rmtree("Lib")


def build_app(*, production: bool = False) -> None:
    os.environ["PYTHONUTF8"] = "1"

    if production:
        print("Building app...")

    # Mirror the public files of the user to the build files
    shutil.copytree("public", "build" if production else "_pyfyre", dirs_exist_ok=True)

    create_pages(production=production)
    bundle_scripts(production=production)
    add_cpython_packages(production=production)

    if production:
        print("App successfully built.")
