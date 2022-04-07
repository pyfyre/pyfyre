"""PyFyre States"""

from pyfyre.core.initializeEnvironment import initializeEnvironment
from pyfyre.globals import Globals
from pyfyre.core.exceptions import RenderError

class UsesState:
    """Create a component that is stateful.

    If you think the component will update again and again,
    you might want to use [UsesState] for that component.

    This allows you to rerender the component when data
    changes by calling `self.update()` method.

    This also wraps the uncaught errors on `self.onerror` method
    where you can also override and create your own UI error.

    Your [UsesState] method must override the build method returning
    an another component or a Widget.
    """

    def __init__(self):
        self.domElement = None
        self.initializedDom = False
    
    def build(self):
        pass

    def dom(self):
        try:
            if not self.initializedDom: self.initState()
            self.domElement = self.build().dom()
            self.initializedDom = True
            return self.domElement
        except Exception as e:
            if Globals.DEBUG: raise e
            
            self.domElement = self.onerror(e).dom()
            return self.domElement

    def initState(self):
        """
        This method is called when the component first
        renders on the screen.

        Override this method by declaring another `initState`
        method into your component.
        """
        pass

    def onerror(self, e):
        """
        Handle errors on every component separately. When an error
        interrupts the `build` method on the component, this `onerror`
        method will be fired and you can handle it professionally without
        blowing the entire app.
        
        Override this method by declaring another `onerror` method on your
        component and taking another parameter where the error exception will
        pass. You must return a widget in which the UI you want your
        users to see temporarily.
        """
        
        return RenderError("Oh no! Something went wrong. We're working on fixing it.", e)

    def update(self):
        """
        Updates the DOM element. Instead of painting the app again
        for state change, only update the DOM where the change happens.
        """
        
        parentNode = self.domElement.parentNode
        self.domElement.remove()
        self.domElement = self.dom()
        parentNode.appendChild(self.domElement)


class State:
    """
    Creates a new state. State objects can store values in Python dictionary
    you can access these values easily.

    Parameters
    ----------
    values : str, int, or dict.
        Used to initialize a State

    Attributes
    ----------
    If you passed a dictionary, you can access the value of a key
    by just calling it like a property

    For instance:
    `state = State({ "count": 0 })`

    Then you can call it:
    `state.count`

    For changing the value of it, just:
    `state.count = state.count + 1`

    If you didn't passed a dict, string or integer for instance, you can access
    them by just calling the value property:

    `state = State(0)`

    Call it:

    `state.value`
    """
    def __init__(self, values):
        self.values = values

        if not isinstance(values, dict):
            self.setValue("value", values)
            return

        for k, v in self.values.items():
            self.setValue(k, v)

    def setValue(self, of, to):
        setattr(self, of, to)