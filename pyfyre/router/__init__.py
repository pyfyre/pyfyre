from pyfyre.globals import Globals
from pyfyre.globals.events import Events
from pyfyre.pyfyre import runApp

from browser import window, bind

class Router:
    """Router v0.3-alpha.
    
    Creates a wrapper object with window location
    history listener that when it's changed,
    the whole app rerenders and get the provided
    routes and map it correctly.

    Parameters
    ----------
    routes : dict
        A dictionary of object routes. Every value
        must inherit the [UsesState] object.

        For instance:
            Router(
                routes={
                    `"/": Home()`,
                    `"/about": About()`,

                    # Dynamic routing, `:<param>` tells the Router that the `about` path has `<param>` dynamic route.
                    `"/about/:id": AboutPerson()`
                }
            )

    Attributes
    ----------
    query : str
        If dynamic routing is allowed to the route, you can
        get the query of the route.

        For instance:
        `https://www.nicebookies.com/users/hi_mom`

        -----

        from pyfyre.router import Router

        Router(
            routes={
                `"/users/:slug": UserProfile()`,
            }
        )

        -----
        
        from pyfyre.router import Router

        class UserProfile(UsesState):
            def build(self):
                query = Router.query()

                return Text(f"Username: {query['slug']}")

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

            try:
                query = pathname[-1]
                pathurl = pathname[-2]
                
                if query[0] == ":":
                    queryName = query.replace(":", "")
                    Globals.DYNAMIC_ROUTES.append([pathurl, queryName, view])
            except IndexError: ...
        
    def dom(self):
        
        try:
            dom = self.routes[Globals.__LOC__].dom()
        except KeyError:
            try:
                _, pathurl = self.get_params()

                for route in Globals.DYNAMIC_ROUTES:
                    if route[0] == pathurl:
                        dom = route[2].dom()
            except Exception as e:
                # TODO: Create a 404.py that allows developers to customize 404 UI.
                # that can also be modified on the settings so they can
                # customize the 404.py name for their like.
                raise Exception("Path 404: Cannot find the path.")

        return dom

    def listenRoute(self):
        def changeRoute():
            runApp(Globals.__PARENT__)

        Events.addListener("change_route", changeRoute)

    @staticmethod
    def query():
        query, pathurl = Router.get_params(Router)
        
        queryNames = {}

        for route in Globals.DYNAMIC_ROUTES:
            if route[0] == pathurl:
                queryNames[route[1]] = query

        return queryNames

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

    def get_params(self):
        path = f"{Globals.__LOC__}"
        pathname = path.split('/')

        query = pathname[-1]
        pathurl = pathname[-2]

        return query, pathurl