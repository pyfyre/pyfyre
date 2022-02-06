
class Globals:

    # The Parent of all widgets object stored here
    # from `runApp`'s first parameter.
    __PARENT__ = None


    # The current pathname location used for routing.
    __LOC__ = None

    # Dynamic routes
    DYNAMIC_ROUTES = []
    
    # For checking if it's the first time initializing the Router
    PATH_INITIALIZED = False


    # All the event objects for firing.
    __EVENTS__ = {}


    # Path of Assets folder
    __ASSETS__ = ""