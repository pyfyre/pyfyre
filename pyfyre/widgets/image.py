from pyfyre.widgets.widget import Widget

class Image(Widget):
    """Creates an Image widget.

    Attributes
    ----------
    src : str (positional)
        The link of the image.
    """

    def __init__(self, src, className="", props: dict={}):
        props["src"] = src
        super().__init__("img", className="", props=props)