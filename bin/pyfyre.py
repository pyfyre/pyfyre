#!/usr/bin/env python3

import os
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
    copy_tree(core_dir, os.path.join(path, "pyf-modules"))
    
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

def liveserver(port: int=8080):
    from livereload import Server
    server = Server()
    server.watch(os.path.join(os.getcwd(), "src", "*"))
    server.serve(port=port, host="localhost")

def main(argv=None):
    """Entry Point"""
    try:
        if argv[1] == "create-app":
            try:
                name = argv[2]
            except IndexError:
                name = "MyApp"
            
            try:
                description = argv[3]
            except IndexError:
                description = "PyFyre web application."
            
            create_app(name, description)
        elif argv[1] == "runserver":
            try:
                liveserver(port=int(argv[2]))
            except IndexError:
                liveserver()
        elif argv[1] == "help":
            pyfyre_help()
        else:
            pyfyre_help()
    except IndexError:
        pyfyre_help()

if __name__ == "__main__":
    main()
