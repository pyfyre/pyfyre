"""
This module is a server for developing PyFyre on your local environment.
This creates a PyFyre app in the directory called `__dev__` and
detects changes on `pyfyre` folder and automatically produce the
js file to replace the current one on the app without the need of
recreating PyFyre apps again and again.
"""

from shutil import rmtree
from livereload import Server
from pyfyre.management import ManagementUtility
import os, subprocess, threading

def main():
    print("Starting PyFyre contributor development environment...")

    os.system("title Contrib Server")

    server = Server()

    management = ManagementUtility()

    if os.path.exists("__dev__"): rmtree("__dev__")
    
    management.create_app("__dev__", "Contributor development environment")

    _directory = os.path.join(os.getcwd())

    def reload():
        print("Reloading, producing js...")

        os.chdir(os.path.join(os.getcwd(), "..", "pyfyre"))
        os.system("brython-cli --make_package pyfyre")

        with open(os.path.join("pyfyre.brython.js")) as file:
            content = file.read()
        with open(os.path.join(_directory, "pyf_modules", "modules.js"), "w") as file:
            file.write(content)

        os.remove("pyfyre.brython.js")

        print("Success!")

    print(f"PyFyre server for contributing development kit")

    def run():
        subprocess.call('start /wait pyfyre runapp && title PyFyre Server', shell=True)

    app_thread = threading.Thread(target=run)
    app_thread.start()

    while True:
        command = input("PyFyre CDK >> ")

        if command.lower() == "s":
            reload()

if __name__ == '__main__': main()