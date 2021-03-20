#!usr/bin/env python

from shutil import copyfile

import http.server
import socketserver

import sys
import os
import time
import threading

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

def create_app(app_name):
    try:
        APP_NAME = app_name if not app_name == "" else input("What is the name of the project? ")
        DESCRIPTION = input("What is the description? ")

        # Get the Path
        PATH = os.path.join(os.getcwd(), APP_NAME)
    except:
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
    manager = open(os.path.join(PATH, APP_NAME, "manager.py")< "w+")
    
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
    """# Import PyNani
from pynani.core.pynani import Component, RunApp
from pynani.core.widgets import Widgets

widgets = Widgets()

# Create class called MyApp extends Component from PyNani Core
class MyApp(Component):

    # Where all rendering stuff began in a component...
    def build(self):

        # Returing widgets.container A.K.A <div> in HTML
        # widgets.container(child[Widget], onClick[Javascript], styles[List of CSS Styles])
        return widgets.container(

            # With a child widgets.header1 A.K.A <h1> in HTML
            # widgets.header1(text[String], onClick[Javascript], styles[List of CSS styles])
            child=widgets.header1(
                text="Hello, Jabez!",
                styles=[
                    "margin-top: 10px"
                ]
            )
        )

## To render the widgets into the screen, you need to call RunApp() to compile your code into raw HTML
RunApp(MyApp())
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

    settings.writelines(f"""app_name: {APP_NAME}
description: {DESCRIPTION}
    """)

    manager.writelines("""from pynani.bin import pynani
import os
import sys

print(sys.argv[1])

if sys.argv[1] == "create-app":
	try:
		pynani.create_app(sys.argv[2])
	except:
		pynani.create_app("My Nani App")
elif sys.argv[1] == "runserver":
	try:
		pynani.run_server(sys.argv[2])
	except:
		pynani.runserver()
elif sys.argv[1] == "":
	pynani.help()
    """)

    # close the files
    main.close()
    indexHTML.close()
    settings.close()
    readme.close()
    manager.close()

    print("App created successfully!")

def run_server(port):
    server = threading.Thread(target=server_start, args=(port,))
    file_watcher = threading.Thread(target=file_watching, args=())

    file_watcher.start()
    server.start()
    file_watcher.join()
    server.join()
    
def file_watching():
    main_path = os.path.join(os.getcwd(), "src", "main.py")
    print(f"I am the Path: {main_path}")
    exec(open(main_path).read())
    print("Heating up the Hot Reload, current is Cold Reload.")
    time.sleep(1)
    PATH = main_path.replace("main.py", "")
    
    class MyHandler(FileSystemEventHandler):
        def __init__(self):
            self.debounce = False

        def on_modified(self, event):
            if not self.debounce:
                self.debounce = True
                print("Changes detected! Hot reloading...")
                exec(open(main_path).read())
                print("Hot reloaded!")
                time.sleep(5)
                self.debounce = False

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=PATH, recursive=True)
    observer.start()
    print("Hot Reload is now Hot!")
    print("Now watching for file changes with WatchDog\n")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

def server_start(port):
    PORT = port if port == "" else 8000

    web_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'core', "public"))

    os.chdir(web_dir)

    handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"Server now started at localhost: {PORT}")
        print("PyNani version that you're currently using is 1.0.0-alpha")
        print("To quit the server or to turn off exit the command-line")
        print("Thank you!")
        httpd.serve_forever()
