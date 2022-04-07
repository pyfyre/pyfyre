from pyfyre.widgets.widget import Widget
from browser import bind

class Events:
    MOUSE_OVER = "mouseover"

class WidgetEvent:    
    def __init__(self, child, event, onEvent):
        self.child = child
        self.event = event
        self.onEvent = onEvent
    
    def dom(self):
        element = self.child.dom()

        @bind(element, self.event)
        def bindWrapper(e):
            self.onEvent(e)

        return element