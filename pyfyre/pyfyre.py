from browser import document
from pyfyre.globals import Globals

def runApp(app, mount="app-mount"):
    body = document.getElementById(mount)
    body.innerHTML = ""
    body.appendChild(app.dom())

    Globals.__PARENT__ = app