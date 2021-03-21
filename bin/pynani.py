#!/usr/bin/env python3

from shutil import copyfile

import http.server
import socketserver

import os
import sys
import time
import threading
from os.path import join as path

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except ImportError:
    pass

PATH = ""

def pynani_help():
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

def create_app(app_name, description):
    APP_NAME = app_name
    DESCRIPTION = description

    # Get the Path
    PATH = path(os.getcwd(), APP_NAME)
    
    print("Creating your PyNani App")

    # Create the Main Folder
    os.makedirs(PATH)

    # Create the SRC PATH
    os.makedirs(path(PATH, APP_NAME, "src"))

    # Create the Files
    main = open(path(PATH, APP_NAME, "src", "main.py"), "w+")
    indexHTML = open(path(PATH, APP_NAME, "index.html"), "w+")
    settings = open(path(PATH, APP_NAME, "settings.yaml"), "w+")
    manager = open(path(PATH, APP_NAME, "manager.py"), "w+")
    
    # Create README.md
    readme = open(path(PATH, APP_NAME, "README.md"), "w+")

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

try:
    print(sys.argv[1])
    
    if sys.argv[1] == "create-app":
        try:
            name = sys.argv[2]
        except IndexError:
            name = "My App"
        
        try:
            description = sys.argv[3]
        except IndexError:
            description = "My PyNani application."
        
        pynani.create_app(name, description)
    elif sys.argv[1] == "runserver":
        pynani.runserver()
except IndexError:
    pynani.pynani_help()
    
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
    main_path = path(os.getcwd(), "src", "main.py")
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

    web_dir = os.path.abspath(path(os.path.dirname( __file__ ), '..', 'core', "public"))

    os.chdir(web_dir)

    handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"Server now started at localhost: {PORT}")
        print("PyNani version that you're currently using is 1.0.0-alpha")
        print("To quit the server or to turn off exit the command-line")
        print("Thank you!")
        httpd.serve_forever()

# Entry Point
try:
    if sys.argv[1] == "create-app":
        try:
            name = sys.argv[2]
        except IndexError:
            name = "My App"
        
        try:
            description = sys.argv[3]
        except IndexError:
            description = "My PyNani application."
        
        create_app(name, description)
except IndexError:
    pynani_help()
