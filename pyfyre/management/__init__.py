#!/usr/bin/env python3

import os, sys, random, string, time
from shutil import copytree, rmtree
from distutils.dir_util import copy_tree

class ManagementUtility:
    def pyfyre_help(self):
        PYFYRE_HELP = """Manage your PyFyre projects.

        Common Commands:

            pyfyre.py create-app [name] [description]
                Create a new PyFyre project in your current directory.

            pyfyre.py runserver [port=8080]
                Run a live server in your current directory.

            pyfyre.py help
                Show this message.
        """
        print(PYFYRE_HELP)

    def create_app(self, app_name: str, app_description: str):
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
            content = file.read().format(app_name=app_name, app_description=app_description, main_key="{main_key}")
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

        os.system("brython-cli --install")

        # Remove unused files produced by Brython
        os.remove("demo.html")
        os.remove("unicode.txt")
        os.remove("README.txt")
        os.remove("brython.js")
        os.remove("index.html")

        rmtree(os.path.join(path, "pyfyre", "management"))
        rmtree(os.path.join(path, "pyfyre", "user"))

        os.system("brython-cli --make_package pyfyre")
        os.remove("pyfyre.py")
        os.system("brython-cli --modules")

        os.chdir(os.path.join(".."))
        os.mkdir("pyf_modules")

        with open(os.path.join(path, "pyfyre", "brython_modules.js")) as file:
            content = file.read()
        with open(os.path.join("pyf_modules", "builtins.js"), "w") as file:
            file.write(content)
        with open(os.path.join(path, "pyfyre", "pyfyre.brython.js")) as file:
            content = file.read()
        with open(os.path.join("pyf_modules", "modules.js"), "w") as file:
            file.write(content)
        
        rmtree("pyfyre")
        os.system("cls" if os.name == "nt" else "clear")
        
        print("Project created successfully.")

    def produce(self, directory_path, build_path, reload=False):

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

            copytree(css_path, src_css_path)

        with open(os.path.join(build_path, "index.html")) as file:
            index_content = file.read()

        # Produce the necessary standard library for Brython
        os.chdir(os.path.join(directory_path, "src"))
        os.system("brython-cli --make_package src")

        # Write files to build directory
        with open(os.path.join("src.brython.js")) as file:
            content = file.read()
        with open(os.path.join(build_path, "src.brython.js"), "w") as file:
            file.write(content)
        with open(os.path.join(build_path, "index.html"), "w") as file:
            file.write(index_content)
        with open(os.path.join(directory_path, "src", "__init__.py")) as file:
            content = file.read()
        with open(os.path.join(build_path, "__init__.py"), "w") as file:
            file.flush()
            file.write(content)

        os.remove("src.brython.js")

        os.chdir(build_path)
        
        # Remove the reloading files for refresh
        if reload:

            _ignores = set(["__serve__", "__dev__"])

            # Remove the src files
            for _, dirs, filenames in os.walk(build_path):
                [dirs.remove(tmp) for tmp in list(dirs) if tmp in _ignores]

                for filename in filenames:
                    name, ext = os.path.splitext(filename)

                    if ext == ".js":
                        if "main" in name:
                            with open(os.path.join(build_path, "src.brython.js")) as file:
                                content = file.read()
                            with open(filename, "w") as file:
                                file.write(content)

            # Refresh the css files
            css_path = os.path.join(directory_path, "src", "css")
            src_css_path = os.path.join(build_path, "css")

            rmtree(src_css_path)

            src_css_path = os.path.join(build_path, "css")

            copytree(css_path, src_css_path)

        # Remove unnecessary files
        if not reload:
            try:
                rmtree("__serve__")
                rmtree("__pycache__")

                os.remove("requirements.txt")
                os.remove("runtime.txt")
            except Exception: pass

            rmtree("pyf_modules")
            os.remove("README.md")
            os.remove("settings.yaml")

            rmtree("src")

    def run_app(self, directory, port):
        print("Running your app in a development server...")

        try:
            from livereload import Server
        except ImportError:
            raise ImportError("Cannot find the liveserver module. Is it installed?")

        server = Server()

        _directory = os.path.abspath(directory) if directory else os.getcwd()
        
        if os.path.exists(os.path.join(_directory, "__serve__")):
            rmtree(os.path.join(_directory, "__serve__"))
        
        _build = os.path.join(_directory, "__serve__")

        def reload():
            print("Detected file changes, performing hot reload...")
            self.produce(_directory, _build, reload=True)
            self.produceJsBundle(_build)
            print("Hot reload successful!")

        self.produce(_directory, _build)
        self.produceJsBundle(_build)

        os.system("cls" if os.name == "nt" else "clear")
        
        print("Happy Hacking!")

        server.watch(f"{_directory}/src/", reload)
        server.serve(port=port if port else 8000, host="localhost", root=os.path.join(_directory, "__serve__"))

    def build_app(self, directory):
        print("Producing optimized build for your project...")

        directory_path = os.path.abspath(directory) if directory else os.getcwd()

        if os.path.exists(os.path.join(directory_path, "build")):
            rmtree(os.path.join(directory_path, "build"))

        build_path = os.path.join(directory_path, "build")

        self.produce(directory_path, build_path)
        self.produceJsBundle(build_path)

        print("Build succeeded!")

    def produceJsBundle(self, build_path):

        try:
            import js2py
        except ImportError:
            raise ImportError("Cannot find js2py. Is it installed?")

        os.chdir(build_path)

        main = {}

        ctx_main = js2py.EvalJs()
        ctx_std = js2py.EvalJs()
        ctx_pyf = js2py.EvalJs()

        with open(os.path.join(build_path, f"src.brython.js")) as file:
            content = file.readlines()
            content.pop(0)
            content.pop(1)
            main_js = ''.join(content)
        with open(os.path.join(build_path, f"builtins.js")) as file:
            content = file.readlines()
            content.pop(0)
            content.pop(0)
            content.pop(1)
            std_js = ''.join(content)
        with open(os.path.join(build_path, f"modules.js")) as file:
            content = file.readlines()
            content.pop(0)
            content.pop(1)
            pyf_js = ''.join(content)


        ctx_main.execute(main_js)
        ctx_std.execute(std_js)
        ctx_pyf.execute(pyf_js)

        main_scripts = ctx_main.scripts.to_dict()
        std_scripts = ctx_std.scripts.to_dict()
        pyf_scripts = ctx_pyf.scripts.to_dict()

        def loopThroughDict(sc):
            for k, v in list(sc.items()):
                if k == "$timestamp":
                    sc.pop(k)
                
                main[k] = v

        loopThroughDict(main_scripts)
        loopThroughDict(std_scripts)
        loopThroughDict(pyf_scripts)

        main_key = ''.join(random.choice(string.ascii_lowercase) for i in range(15))

        with open(os.path.join(build_path, f"main.{main_key}.js"), "w") as file:
            main["$timestamp"] = time.time()

            brython = [
                "__BRYTHON__.use_VFS = true;\n",
                f"var scripts = {str(main)}",
                "\n__BRYTHON__.update_VFS(scripts)"
            ]
            
            file.writelines(brython)

        with open(os.path.join(build_path, "index.html")) as file:
            content = file.read().format(main_key=main_key)
        with open(os.path.join(build_path, "index.html"), "w") as file:
            file.write(content)

        os.remove(f"src.brython.js")
        os.remove(f"modules.js")
        os.remove(f"builtins.js")

def execute_from_command_line(argv=None):
    utility = ManagementUtility()

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
            
            utility.create_app(name, description)
        elif sys.argv[1] == "runapp":
            try:
                port = sys.argv[2]
            except IndexError:
                port = None

            try:
                directory = sys.argv[3]
            except IndexError:
                directory = None

            utility.run_app(directory, port)
        elif sys.argv[1] == "build":
            try:
                directory = sys.argv[2]
            except IndexError:
                directory = None

            utility.build_app(directory)
        elif sys.argv[1] == "help":
            utility.pyfyre_help()
        else:
            utility.pyfyre_help()
    except IndexError as e:
        utility.pyfyre_help()

if __name__ == "__main__":
    execute_from_command_line()
