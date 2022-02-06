from pyfyre.globals import Globals
from pyfyre.globals.events import Events
from pyfyre.pyfyre import runApp

from browser import document, window, bind

class Router:
    """Router v0.3-alpha.
    
    Creates a wrapper object with window location
    history listener that when it's changed,
    the whole app rerenders and get the provided
    routes and map it correctly.

    Attributes
    ----------
    routes : dict
        A dictionary of object routes. Every value
        must inherit the [UsesState] object.

        For instance:
            Router(
                routes={
                    `"/": Home()`,
                    `"/about": About()`,

                    # Dynamic routing, `<>` tells the Router that the `about` path has dynamic routes.
                    `"/about/<>: AboutPerson()`
                }
            )

    query : str
        If dynamic routing is allowed to the route, you can
        get the query of the route.

        For instance:
        `https://www.nicebookies.com/users/users_cool_username`

        -----

        from pyfyre.router import Router

        Router(
            routes={
                `"/users/<>": UserProfile()`,
            }
        )

        -----
        
        from pyfyre.router import Router

        class UserProfile(UsesState):
            def __init__(self):
                self.username = Router.query

            def build(self):
                return Text(f"Username: {self.username}")

    """

    def __init__(self, routes):
        self.routes: dict = routes

        if not Globals.PATH_INITIALIZED:
            Globals.__LOC__ = window.location.pathname
            Globals.PATH_INITIALIZED = True

        if not "change_route" in Globals.__EVENTS__:
            Events.add("change_route")

            self.listenRoute()

        for routeName, view in self.routes.items():
            pathname = routeName.split('/')

            query = pathname[-1]
            pathurl = pathname[-2]

            if query == "<>":
                Globals.DYNAMIC_ROUTES.append([pathurl, view])
        
    def dom(self):

        try:
            dom = self.routes[Globals.__LOC__].dom()
        except KeyError:
            try:
                pathurl = self.pathurl

                for route in Globals.DYNAMIC_ROUTES:
                    if route[0] == pathurl:
                        dom = route[1].dom()
            except Exception:
                # TODO: Create a 404.py that allows developers to customize 404 UI.
                # that can also be modified on the settings so they can
                # customize the 404.py name for their like.
                raise Exception("PATH 404: Cannot find the path.")

        return dom

    def listenRoute(self):
        def changeRoute():
            runApp(Globals.__PARENT__)

        Events.addListener("change_route", changeRoute)

    @property
    def query(self):
        path = f"{Globals.__LOC__}"
        pathname = path.split('/')
        query = pathname[-1]

        return query

    @property
    def pathurl(self):
        path = f"{Globals.__LOC__}"
        pathname = path.split('/')
        pathurl = pathname[-2]

        return pathurl

    @staticmethod
    def push(location):
        Globals.__LOC__ = location

        Events.broadcast("change_route")
        window.history.pushState(None, None, location)

        @bind(window, 'popstate')
        def popState(e):
            Globals.__LOC__ = window.location.pathname
            Events.broadcast("change_route")
            e.preventDefault()