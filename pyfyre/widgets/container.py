from pyfyre.widgets.widget import Widget

class Container(Widget):
    """Creates a Container Widget.

    This is like `div` in HTML.

    Attributes
    ----------
    children : list<Widget>
        The list of children of the Container widget.
    """
    
    def __init__(self, children=[], className="", props: dict=None):
        super().__init__("div", className=className, props=props)
        self.children = children
    
    def dom(self):
        element = super().dom()
        
        for child in self.children:
            element.appendChild(child.dom())
        
        return element