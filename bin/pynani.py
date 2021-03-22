#!/usr/bin/env python3

# standard imports
import os
import sys
import time
import threading
import http.server
import socketserver
from os.path import join as path
from distutils.dir_util import copy_tree

# third-party imports
try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except ImportError:
    pass

VERSION = "1.0.0-alpha"

def pynani_help():
    print("""
Manage your PyNani development.

Common commands:

    pynani.py create-app <app_name> <app_description>
        Creates a new app in where you're located in the CMD
    
    pynani.py runserver
        Runs the Hot Reload WatchDog for watching the file changes and rerender

Usage: pynani.py <command> [arguments]

Available commands:
    create-app        Creates an new project app.
    runserver         Runs the Hot Reload WatchDog for watching the file changes and rerender
    help              For help
""")

def create_app(app_name: str, description: str):
    PATH = path(os.getcwd(), app_name) # get the path
    
    print("Creating your PyNani app...")
    
    os.makedirs(PATH) # Create the user's project directory
    
    # Copy the `core/user` contents to the user's project directory
    user_dir = os.path.abspath(path(os.path.dirname(__file__), "..", "core", "user"))
    copy_tree(user_dir, PATH)
    
    # Create the `settings.yaml` file
    with open(path(PATH, "settings.yaml"), "w+") as file:
        file.writelines(f"app_name: {app_name}\ndescription: {description}\n")
    
    print("App created successfully!")

def run_server(port):
    server = threading.Thread(target=server_start, args=(port, ))
    file_watcher = threading.Thread(target=file_watching)
    file_watcher.start()
    server.start()
    file_watcher.join()
    server.join()

def file_watching():
    main_path = path(os.getcwd(), "src", "main.py")
    
    print(f"I am at the path: {main_path}")
    exec(open(main_path).read())
    print("Heating up the Hot Reload, currently in Cold Reload.")
    
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

def server_start(port: str):
    PORT = int(port) if port else 8000
    web_dir = os.path.abspath(path(os.path.dirname(__file__), "..", "core", "public"))

    os.chdir(web_dir)

    handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"Server now started at localhost: {PORT}")
        print(f"PyNani version that you're currently using is {VERSION}")
        print("To stop the server, press CTRL+C or exit the command-line")
        print("Thank you!")
        httpd.serve_forever()

def main():
    """Entry Point"""
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

if __name__ == "__main__":
    main()
