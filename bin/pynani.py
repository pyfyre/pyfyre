#!/usr/bin/env python

from shutil import copyfile
import sys
import os
import time

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except:
    pass

os.system("cls" if os.name == "nt" else "clear") # supports both Windows and Linux

PATH = ""

def help():
    print("""
Manage your PyNani development.

Common commands:

    pynani.py create-app <app_name>
        Creates a new app in where you're located in the CMD
    
    pynani.py runserver
        Runs the Hot Reload WatchDog for watching the file changes and rerender

Usage: pynani.py <command> [arguments]

Available commands:
    create-app        Creates an new project app.
    runserver         Runs the Hot Reload WatchDog for watching the file changes and rerender
    help              For help
    """)

try:
    if sys.argv[1] == "create-app":
        try:
            APP_NAME = sys.argv[2]

            # Get the Path
            PATH = os.path.join(os.getcwd(), sys.argv[2])
        except IndexError:
            print("""Needs an app name.

Usage: pynani.py create-app <App_Name>""")

            exit()
        
        print("Creating your PyNani App")

        # Create the Main Folder
        os.makedirs(PATH)

        # Create the SRC PATH
        os.makedirs(os.path.join(PATH, APP_NAME, "src"))

        # Create the Files
        main = open(os.path.join(PATH, APP_NAME, "src", "main.py"), "w+")
        indexHTML = open(os.path.join(PATH, APP_NAME, "index.html"), "w+")
        settings = open(os.path.join(PATH, APP_NAME, "settings.yaml"), "w+")
        
        # Create README.md
        readme = open(os.path.join(PATH, APP_NAME, "README.md"), "w+")

        # Write to readme
        readme.writelines("""# PyNani
        Python web UI framework for building nice websites.

        ## THANK YOU!
        Thank you for using PyNani! Your journey using PyNani begins here.

        I am the creator of PyNani, Jabez Borja, I am assuming that you saw this framework in Programming Philippines group.
        I, the creator of this Framework, thanks you for using or trying this Framework that I created. I appreciate it, sooo much!

        If you have any questions, suggestions or bug reports about this Framework, please make an issue on Github repo, or email me at jabez.natsu@gmail.com.

        Again, thank you and enjoy!

        """)

        # Write as the starter of Main.py
        main.writelines(
        """from PyNani import PyNani, utils

        ## Creates an instance for PyNaniDOM
        pyNaniDOM = PyNani.PyNaniDOM()
        ## Also here.
        utils = utils.Utils()

        ## Creates a function returning a header1, it is equal to
        ## <h1> in HTML, utils.header1 is finding arguments:
        ## (text[String], onClick[Javascript function], styles[List of CSS styles])
        def HelloMessage(message):
            return utils.header1(
                text="Hello, %s!" % message,
            )

        ## Here where all UI began to render in the screen.
        ## render is finding argument called props.
        ## (props[list of elements to render])
        pyNaniDOM.render(
            props=[
                HelloMessage("Hello, World!"),
            ]
        )
        """
        )

        # Write as the starter of index.html
        indexHTML.writelines("""
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title></title>
    </head>
    <body>
        
    </body>
    <footer>
    </footer>
    <style>
        body {
            padding: 0;
            margin: 0;
        }
    </style>
</html>
        """)
        
        # close the files
        main.close()
        indexHTML.close()
        settings.close()
        readme.close()
        
        print("App created successfully!")
    elif sys.argv[1] == "runserver":
        os.system("py main.py")
        os.system("color a")
        print("Heating up the Hot Reload, current is Cold Reload.")
        time.sleep(1)
        PATH = os.getcwd()
        
        class MyHandler(FileSystemEventHandler):
            def __init__(self):
                self.debounce = False

            def on_modified(self, event):
                if not self.debounce:
                    self.debounce = True
                    print("Changes detected! Hot reloading...")
                    os.system("py main.py")
                    print("Hot reloaded!")
                    time.sleep(5)
                    self.debounce = False

        event_handler = MyHandler()
        observer = Observer()
        observer.schedule(event_handler, path=PATH, recursive=True)
        observer.start()
        print("Hot Reload is now Hot!")
        print("Now watching for file changes with WatchDog\n")
        print("PyNani version that you're currently using is 1.0.0-alpha")
        print("To quit the server or to turn off CTRL-BREAK")
        print("Thank you!")
        print
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
    elif sys.argv[1] == "help":
        help()
except Exception as e:
    if e == "list index out of range":
        help()
    