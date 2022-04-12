from pyfyre.widgets.widget import Widget

class Image(Widget):
    """Creates an Image widget.

    Attributes
    ----------
    src : str (positional)
        The link of the image.
    """

    def __init__(self, src, attrs: dict=None):
        attrs["src"] = src
        super().__init__("img", attrs=attrs)