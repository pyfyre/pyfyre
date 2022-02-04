from pyfyre.widgets.widget import Widget

class Image(Widget):
    
    def __init__(self, src, className="", props: dict=None):
        super().__init__("img", className=className, props=props)
        self.src = src
    
    def dom(self):
        element = super().dom()
        element.src = self.src
        
        return element