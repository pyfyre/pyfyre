from pyfyre.widgets.widget import Widget

class Clickable(Widget):
    
    def __init__(self, bind, onclick, className="", props: dict=None):
        super().__init__("div", className=className, props=props)
        self.bind = bind
        self.onclick = onclick
    
    def dom(self):
        element = super().dom()
        
        element.appendChild(self.bind.dom())

        element.bind("click", self.onclick)
        
        return element