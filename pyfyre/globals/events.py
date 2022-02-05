from pyfyre.globals import Globals

class Events:
    """
    Creates an event and add listeners to it. Listeners are unfired methods.
    If an event fires off on `broadcastEvent` method, every listener of
    that event will be fired off.

    Methods
    -------
    add(event: str)
        Add a global event.

    addListener(event: str, listener: method)
        Add listener to the given [event].

    broadcast(event: str)
        Cast the event and fire all the listener methods

    """

    @staticmethod
    def add(event):
        """Create a global event.

        Parameters
        ----------
        event : str
            The name of the event.
        """
        Globals.__EVENTS__[event] = []

    @staticmethod
    def addListener(event, listener):
        """Add listener to a global event.

        Parameters
        ----------
        event : str
            The name of the event.
        listener : method
            The listener to the event that fires off when
            the event has been broadcast.
        """
        Globals.__EVENTS__[event].append(listener)

    @staticmethod
    def broadcast(event):
        """Broadcast the global event.

        Parameters
        ----------
        event : str
            The name of the event to be broadcast.
        """
        for func in Globals.__EVENTS__[event]:
            func()