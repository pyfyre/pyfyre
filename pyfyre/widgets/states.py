"""PyFyre States"""

from pyfyre.widgets.widget import Widget
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
    
    def build(self):
        pass

    def dom(self):
        try:
            self.domElement = self.build().dom()
            return self.domElement
        except Exception as e:
            self.domElement = self.onerror(e).dom()
            return self.domElement

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
        
        print("ERR!", e)

        return RenderError("Oh no! Something went wrong. We're working on fixing it.")

    def update(self):
        """
        Updates the DOM element. Instead of painting the app again
        for state change, only update the DOM where the change happens.
        """
        
        parentNode = self.domElement.parentNode
        self.domElement.remove()
        self.domElement = self.dom()
        parentNode.appendChild(self.domElement)