from pyfyre.widgets.widget import Widget

class Text(Widget):
    
    def __init__(self, textContent: str, className="", props: dict=None):
        super().__init__("p", className=className, props=props)
        self.textContent = textContent
    
    def dom(self):
        element = super().dom()
        element.textContent = self.textContent
        
        return element