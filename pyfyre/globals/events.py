from pyfyre.globals import Globals

class Events:
    """
    Creates an event and add listeners to it. Listeners are unfired methods.
    If an event fires off on `broadcastEvent` method, every listener of
    that event will be fired off.
    """

    @staticmethod
    def add(event):
        Globals.__EVENTS__[event] = []

    @staticmethod
    def addListener(event, listener):
        Globals.__EVENTS__[event].append(listener)

    @staticmethod
    def broadcast(event):
        for func in Globals.__EVENTS__[event]:
            func()