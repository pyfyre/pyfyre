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
    
    def __init__(self, el, child, attrs: dict=None):
        super().__init__(el, attrs=attrs)
        self.child = child