from pyfyre.widgets.widget import Widget

class CustomElement(Widget):
    """Creates a Custom Element.

    The user can provide a custom element name on HTML with this widget.

    Attributes
    ----------
    element : str
        The name of the element, 'div' for instance.
    child : str | list
        The child of the element.
    """
    
    def __init__(self, el, child, className="", props: dict=None):
        super().__init__(el, className=className, props=props)
        self.child = child
    
    def dom(self):
        element = super().dom()

        if isinstance(self.child, str):
            element.textContent(self.child)
            return element

        if isinstance(self.child, list):
            for child in self.child:
                if not isinstance(child, Widget):
                    raise Exception("CustomElement child is not a widget.")

                element.appendChild(child.dom())

        return element