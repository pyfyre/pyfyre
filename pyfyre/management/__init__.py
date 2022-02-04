#!/usr/bin/env python3

import os, sys, random, string
from shutil import copytree, rmtree, move
from distutils.dir_util import copy_tree

PYFYRE_HELP = """
Manage your PyFyre projects.

Common Commands:

    pyfyre.py create-app [name] [description]
        Create a new PyFyre project in your current directory.

    pyfyre.py runserver [port=8080]
        Run a live server in your current directory.

    pyfyre.py help
        Show this message.
"""

def pyfyre_help():
    print(PYFYRE_HELP)

def create_app(app_name: str, app_description: str):
    """Create a PyFyre project."""
    
    print("Creating your PyFyre project...")
    
    path = os.path.join(os.getcwd(), app_name)
    
    try:
        os.makedirs(path)
    except FileExistsError:
        print("Project already exists. Aborted.")
        return
    
    # copy the `core` directory contents to the user's project directory
    core_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    copy_tree(core_dir, os.path.join(path, "pyfyre"))
    
    # copy the `user` directory contents to the user's project directory
    user_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "user"))
    copy_tree(user_dir, path)
    
    # edit the `index.html` file
    with open(os.path.join(user_dir, "index.html")) as file:
        content = file.read().format(app_name=app_name, app_description=app_description, pyfyre_key="{pyfyre_key}", src_key="{src_key}")
    with open(os.path.join(user_dir, "index.html"), "w") as file:
        file.write(content)
    
    # edit the `README.md` file
    with open(os.path.join(user_dir, "README.md")) as file:
        content = file.read().format(app_name=app_name, app_description=app_description)
    with open(os.path.join(path, "README.md"), "w") as file:
        file.write(content)
    
    # edit the `settings.yaml` file
    with open(os.path.join(user_dir, "settings.yaml")) as file:
        content = file.read().format(app_name=app_name, app_description=app_description)
    with open(os.path.join(path, "settings.yaml"), "w") as file:
        file.write(content)

    os.chdir(os.path.join(path, "pyfyre"))
    os.system("brython-cli --make_package pyfyre")

    with open(os.path.join("pyfyre.brython.js")) as file:
        content = file.read()

    os.chdir(os.path.join(".."))
    os.mkdir("pyf_modules")
    rmtree("pyfyre")

    with open(os.path.join("pyf_modules", "pyfyre.brython.js"), "w") as file:
        file.write(content)
        
    os.system("cls" if os.name == "nt" else "clear")
    
    print("Project created successfully.")

def produce(directory_path, build_path, reload=False):

    # If it's in the entry point, create a new path for the first time and produce
    # the essential Python js module. This will make the Hot Reload more faster.
    if not reload:
        copytree(directory_path, build_path)

        for _, __, filenames in os.walk(os.path.join(build_path, "pyf_modules")):
            for filename in filenames:

                _, ext = os.path.splitext(filename)

                if ext == ".js":
                    with open(os.path.join(directory_path, "pyf_modules", filename)) as file:
                        content = file.read()
                    with open(os.path.join(build_path, filename), "w") as file:
                        file.write(content)

        # Refresh the css files
        css_path = os.path.join(directory_path, "src", "css")
        src_css_path = os.path.join(build_path, "css")
        os.mkdir(os.path.join(build_path, "__temp__"))

        copytree(css_path, src_css_path)

    with open(os.path.join(build_path, "index.html")) as file:
        index_content = file.read()

    # Produce the necessary standard library for Brython
    os.chdir(build_path)
    os.system("brython-cli --install")

    # Remove unused files produced by Brython
    os.remove(os.path.join(build_path, "demo.html"))
    os.remove(os.path.join(build_path, "unicode.txt"))
    os.remove(os.path.join(build_path, "README.txt"))
    os.remove(os.path.join(build_path, "brython.js"))

    # Produce modules

    if reload: os.chdir(directory_path)

    os.system("brython-cli --modules") 
    
    # Write files to build directory
    with open(os.path.join(build_path, "index.html"), "w") as file:
        file.write(index_content)
    with open(os.path.join(directory_path, "src", "__init__.py")) as file:
        content = file.read()
    with open(os.path.join(build_path, "__init__.py"), "w") as file:
        file.flush()
        file.write(content)

    os.chdir(build_path)
    
    # Remove the reloading files for refresh
    if reload:

        _ignores = set(["__temp__", "__serve__", "__dev__"])

        # Remove the src files
        for _, dirs, filenames in os.walk(build_path):
            [dirs.remove(tmp) for tmp in list(dirs) if tmp in _ignores]

            for filename in filenames:
                name, ext = os.path.splitext(filename)

                if ext == ".js":
                    if "main" in name:
                        with open(os.path.join(build_path, "brython_modules.js")) as file:
                            content = file.read()
                        with open(filename, "w") as file:
                            file.write(content)

        # Refresh the css files
        css_path = os.path.join(directory_path, "src", "css")
        src_css_path = os.path.join(build_path, "css")

        rmtree(src_css_path)

        src_css_path = os.path.join(build_path, "css")

        copytree(css_path, src_css_path)

    if not reload:
        # Rename files for production secret
        modules_key = ''.join(random.choice(string.ascii_lowercase) for i in range(15))
        pyfyre_key = ''.join(random.choice(string.ascii_lowercase) for i in range(15))

        os.rename("brython_modules.js", "main.%s.js" % modules_key)
        os.rename("pyfyre.brython.js", "pyf.%s.js" % pyfyre_key)

        # Format the js script link of the `index.html`
        with open(os.path.join(build_path, "index.html")) as file:
            content = file.read().format(modules_key=modules_key, pyfyre_key=pyfyre_key)
        with open(os.path.join(build_path, "index.html"), "w") as file:
            file.write(content)

    # Remove unnecessary files
    if not reload:
        try:
            os.remove("requirements.txt")
            os.remove("runtime.txt")

            rmtree("__serve__")
            rmtree("__temp__")
            rmtree("__pycache__")
        except Exception: pass

        rmtree("pyf_modules")
        os.remove("README.md")
        os.remove("settings.yaml")
        os.remove("brython_stdlib.js")

        rmtree("src")
    elif reload:
        os.remove("brython_stdlib.js")
        os.remove("brython_modules.js")

def run_app(directory, port):
    print("Running your app in a development server...")

    try:
        from livereload import Server
    except ImportError:
        raise ImportError("Cannot find the liveserver module. Is it installed?")

    server = Server()

    _directory = os.path.abspath(directory) if directory else os.getcwd()

    def checkServes():
        if os.path.exists(os.path.join(_directory, "__serve__")):
            rmtree(os.path.join(_directory, "__serve__"))

    def reload():
        print("Detected file changes, performing hot reload...")

        produce(_directory, _build, reload=True)

        print("Hot reload successful!")

    checkServes()
    
    _build = os.path.join(_directory, "__serve__")

    produce(_directory, _build)

    os.system("cls" if os.name == "nt" else "clear")
    print("Happy Hacking!")

    server.watch(f"{_directory}/src/", reload)
    server.serve(port=port if port else 8000, host="localhost", root=os.path.join(_directory, "__serve__"))

def build_app(directory):
    print("Producing optimized build for your project...")

    directory_path = os.path.abspath(directory) if directory else os.getcwd()
    build_path = os.path.join(directory_path, "build")

    print(directory_path)

    produce(directory_path, build_path)

    print("Build succeeded!")

def execute_from_command_line(argv=None):
    """Entry Point"""
    try:
        if sys.argv[1] == "create-app":
            try:
                name = sys.argv[2]
            except IndexError:
                name = "MyApp"
            
            try:
                description = sys.argv[3]
            except IndexError:
                description = "PyFyre web application."
            
            create_app(name, description)
        elif sys.argv[1] == "runapp":
            try:
                directory = sys.argv[2]
            except IndexError:
                directory = None

            try:
                port = sys.argv[3]
            except IndexError:
                port = None

            run_app(directory, port)
        elif sys.argv[1] == "build":
            try:
                directory = sys.argv[2]
            except IndexError:
                directory = None

            build_app(directory)
        elif sys.argv[1] == "help":
            pyfyre_help()
        else:
            pyfyre_help()
    except IndexError:
        pyfyre_help()

if __name__ == "__main__":
    execute_from_command_line()
