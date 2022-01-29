#!/usr/bin/env python3

import os, shutil, sys
from shutil import copytree
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
    core_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "core"))
    copy_tree(core_dir, os.path.join(path, "pyf_modules"))
    
    # copy the `user` directory contents to the user's project directory
    user_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "user"))
    copy_tree(user_dir, path)
    
    # edit the `index.html` file
    with open(os.path.join(user_dir, "index.html")) as file:
        content = file.read().format(app_name=app_name, app_description=app_description)
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
    
    print("Project created successfully.")

def build_app(directory):
    print("Producing optimized build for your project...")

    directory_path = directory if directory else os.getcwd()
    build_path = os.path.join(directory_path, "build")

    print(build_path)
    
    copytree(directory_path, build_path)

    with open(os.path.join(build_path, "index.html")) as file:
        index_content = file.read()

    os.chdir(build_path)
    os.system("brython-cli --install")
    os.remove("brython_stdlib.js")
    os.remove("demo.html")
    os.remove("unicode.txt")
    os.remove("README.txt")
    shutil.rmtree('/__pycache__', ignore_errors=True)

    # Produce an optimized js to directories
    os.chdir(os.path.join(build_path, "pyf_modules"))
    os.system("brython-cli --make_package pyf_modules")
    os.chdir(os.path.join(build_path, "src"))
    os.system("brython-cli --make_package src")

    os.chdir(build_path)

    with open(os.path.join(build_path, "index.html"), "w") as file:
        file.write(index_content)

    os.system("cls" if os.name == "nt" else "clear")

    print("Build succeeded!")

def liveserver(port: int=8080):
    from livereload import Server
    server = Server()
    server.watch(os.path.join(os.getcwd(), "src", "*"))
    server.serve(port=port, host="localhost")

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
        elif sys.argv[1] == "runserver":
            try:
                liveserver(port=int(sys.argv[2]))
            except IndexError:
                liveserver()
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
    main()
