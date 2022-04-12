class Globals:
    
    DEBUG = False

    MOUNT = None

    # The Parent of all widgets object stored here
    # from `runApp`'s first parameter.
    __DOM__ = None
    __OLDVDOM__ = None

    # The current pathname location used for routing.
    __LOC__ = None

    # Dictionary of mapped routes: {"/route": Component()}
    __ROUTES__ = []

    # All the event objects for firing.
    __EVENTS__ = {}

__all__ = ['Events', 'Globals']