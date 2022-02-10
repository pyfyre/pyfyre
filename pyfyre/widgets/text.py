from pyfyre.widgets.states import State
from pyfyre.widgets.widget import Widget
from pyfyre.globals.events import Events

class Text(Widget):
    """Creates a Text widget.

    This is a simple widget to put a text on the screen.

    Attributes
    ----------
    textContent : str
        The text content of the Text widget
    """
    
    def __init__(self, textContent: str, className="", props: dict=None):
        super().__init__("p", className=className, props=props)
        self.textContent = textContent
    
    def dom(self):
        element = super().dom()

        # If the textContent is a State object, create a listener to the
        # global state event, for when if the state change, this widget
        # will automatically adapt to new state changes and updates the DOM.
        if isinstance(self.textContent, State):
            def stateChange():
                self.element.textContent = self.textContent.value

            Events.addListener(f"state-{id(self.textContent)}", stateChange)
            Events.broadcast(f"state-{id(self.textContent)}") # Broadcast it to adapt the initial value of the State.
            return element

        element.textContent = self.textContent
        
        return element