"""PyFyre States"""

from pyfyre.widgets.widget import Widget

class TextException(Widget):
    
    def __init__(self, error: str, className="", props: dict=None):
        super().__init__("h1", className=className, props=props)
        self.error = error
    
    def dom(self):
        element = super().dom()
        element.textContent = self.error
        
        element.attrs["style"] = "background-color: #efa3a3; width: fit-content; padding: 10px;"
        
        return element

class UsesState:

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

        return TextException("Oh no! Something went wrong. We're working on fixing it.")

    def update(self):
        """
        Updates the DOM element. Instead of painting the app again
        for state change, only update the DOM where the change happens.
        """
        
        parentNode = self.domElement.parentNode
        self.domElement.remove()
        self.domElement = self.dom()
        parentNode.appendChild(self.domElement)