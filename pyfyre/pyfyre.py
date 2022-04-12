from browser import document, window
from pyfyre.core.initializeEnvironment import initializeEnvironment
from pyfyre.globals import Globals
from pyfyre.core.runtime_dom.render import Render

def runApp(vApp, mount="app-mount"):
    """This is the main entry point of your app. You must call this
    with an argument object that inherits [UsesState] or just a simple widget.

    Parameters
    ----------
    app : UsesState (Positional)
        This is what the app will render.
    mount : str
        Where the app will mount on the index.html. This is a provided
        id of a `div` element.
    """
    
    Globals.__OLDVDOM__ = vApp.dom()

    _app = Render.render(Globals.__OLDVDOM__)

    Globals.__DOM__ = _app

    body = document.getElementById(mount)
    body.replaceWith(_app)

    # initializeEnvironment()

    # Globals.__PARENT__ = vApp
    # window.PyFyreDOM.broadcast()