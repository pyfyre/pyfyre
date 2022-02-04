"""
This module is a server for developing PyFyre on your local environment.
This creates a PyFyre app in the directory called `__dev__` and
detects changes on `pyfyre` folder and automatically produce the
js file to replace the current one on the app without the need of
recreating PyFyre apps again and again.
"""

from shutil import rmtree
from livereload import Server
from pyfyre.management import create_app, run_app
import os, subprocess, threading

def main():
    print("Starting PyFyre contributor development environment...")

    server = Server()

    if os.path.exists("__dev__"): rmtree("__dev__")
    
    create_app("__dev__", "Contributor development environment")

    _directory = os.path.join("__dev__")
    _build = os.path.join(_directory, "__serve__")

    def reload():
        print("Detected PyFyre file changes, producing js...")

        os.chdir(os.path.join("pyfyre"))
        os.system("brython-cli --make_package pyfyre")

        with open(os.path.join("pyfyre", "pyfyre.brython.js")) as file:
            content = file.read()
        with open(os.path.join(_build, "pyf_modules", "pyfyre.brython.js"), "w") as file:
            file.write(content)

    print(f"PyFyre server for contributing development is now running on port 5000")

    def run():
        subprocess.call('start /wait pyfyre runapp', shell=True)

    app_thread = threading.Thread(target=run)
    app_thread.start()

    server.watch(f"{os.getcwd()}/pyfyre/", reload)
    server.serve(port=5000, host="localhost", root=os.path.join("__serve__"))

if __name__ == '__main__': main()