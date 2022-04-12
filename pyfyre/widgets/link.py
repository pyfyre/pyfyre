from pyfyre.widgets.widget import Widget

from pyfyre.router import Router

class Link(Widget):
    """Creates a Link widget.

    This widget is used for Routers, if you want to redirect to a [Router] route,
    you must use this widget.

    Attributes
    ----------
    textContent : str (positional)
        The text content of the link widget.
    to : str (positional)
        The link of the route on the Router routes dictionary.
    """
    
    def __init__(self, textContent: str, to='/', external=False, attrs: dict=None):
        super().__init__("a", attrs=attrs)
        self.textContent = textContent
        self.to = to
        self.external = external