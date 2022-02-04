from pyfyre.widgets.widget import Widget

from pyfyre.router import Router

class Link(Widget):
    
    def __init__(self, textContent: str, to='/', className="", props: dict=None):
        super().__init__("a", className=className, props=props)
        self.textContent = textContent
        self.to = to
    
    def dom(self):
        element = super().dom()
        element.textContent = self.textContent
        element.href = "#"
        
        element.bind("click", self.navigate)
        
        return element

    def navigate(self, e):
        e.preventDefault()
        Router.push(self.to)