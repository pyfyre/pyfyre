from pyfyre.globals import Globals
from pyfyre.pyfyre import runApp

from browser import document, window

class Router:
    """
    Router v0.1-alpha.

    TODO: fix `popstate` and add url linking.
    """

    def __init__(self, routes):
        Globals.__LOC__ = document.location.pathname

        self.routes = routes
        self.currentRoute = Globals.__LOC__
        
    def dom(self):
        return self.routes[self.currentRoute].dom()

    @staticmethod
    def push(location):
        Globals.__LOC__ = location

        runApp(Globals.__PARENT__)
        window.history.pushState(None, None, location)

        def popState(e):
            runApp(document.location.pathname)
            e.preventDefault()

        window.bind("onpopstate", popState)