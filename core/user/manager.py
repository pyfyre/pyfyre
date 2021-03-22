from pynani.bin import pynani
import os
import sys

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
        
        pynani.create_app(name, description)
    elif sys.argv[1] == "runserver":
        pynani.runserver()
except IndexError:
    pynani.pynani_help()
