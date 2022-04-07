from pyfyre.widgets.widget import Widget
from browser import bind

class MouseHover:    
    def __init__(self, child, event):
        self.child = child
        self.event = event
    
    def dom(self):
        element = self.child.dom()

        @bind(element, "onmouseover")
        def bindWrapper(e):
            print("Hov")

        return element