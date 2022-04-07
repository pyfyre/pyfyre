from pyfyre.widgets.widget import Widget
from browser import bind

class MouseHover:    
    def __init__(self, child, onHover):
        self.child = child
        self.event = onHover
    
    def dom(self):
        element = self.child.dom()

        @bind(element, "mouseover")
        def bindWrapper(e):
            self.event(e)

        return element