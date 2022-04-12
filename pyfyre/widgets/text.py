from pyfyre.widgets.widget import Widget

class Text(Widget):
    """Creates a Text widget.

    This is a simple widget to put a text on the screen.

    Attributes
    ----------
    textContent : str
        The text content of the Text widget
    """
    
    def __init__(self, textContent: str, attrs: dict=None):
        super().__init__("p", children=textContent, attrs=attrs)
        self.textContent = textContent