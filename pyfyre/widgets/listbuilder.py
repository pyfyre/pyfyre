from pyfyre.widgets.widget import Widget

class ListBuilder(Widget):
    
    def __init__(self, count=1, builder=None, className="", props: dict=None):
        super().__init__("div", className=className, props=props)
        self.count = count
        self.builder = builder
    
    def dom(self):
        element = super().dom()
        
        for i in range(self.count):
            element.appendChild(self.builder(i).dom())
        
        return element
