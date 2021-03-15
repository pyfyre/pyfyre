from shutil import copyfile
import sys
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

os.system("cls")

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
            PATH = os.getcwd() + "\\%s" % sys.argv[2]
        except:
            print("""Needs an app name.

Usage: pynani.py create-app <App_Name>""")

            exit()
        
        print("Creating your PyNani App")

        # Create the Folder
        os.makedirs(PATH)

        # Create the SRC PATH
        src_path = os.makedirs(PATH + "\\%s\\src" % APP_NAME)

        # Create the Files
        main = open("%s\\%s\\src\\main.py" % (PATH, APP_NAME), "w+")
        indexHTML = open("%s\\%s\\index.html" % (PATH, APP_NAME), "w+")

        # Create README.md
        readme = open("%s\\%s\\README.md" % (PATH, APP_NAME), "w+")

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

        pyNaniDOM = PyNani.PyNaniDOM()
        utils = utils.Utils()

        def HelloMessage(message):
            return utils.header1(
                text="Hello, %s!" % message,
            )

        pyNaniDOM.render(
            props=[
                HelloMessage("Hello, World!"),
            ]
        )
        """
        )

        print("App created successfully!")
    elif sys.argv[1] == "runserver":
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
                    os.system("py main.py")
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
    