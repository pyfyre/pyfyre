from pyfyre.widgets.widget import Widget

class Clickable(Widget):
    """Creates a Clickable widget.

    This wraps your widget into a clickable state. Just like InkWell
    in Flutter. Every widget (except Button) has no built-in onClick method
    so to allow then to be clickable, you must wrap them with this [Clickable] widget.

    Attributes
    ----------
    bind : Widget (positional)
        The widget you want to be clickable.
    onClick : method
        The method you provided where when the button has been clicked
        or activate, the [onClick] method will be fired automatically.
    """
    
    def __init__(self, bind, onClick, className="", props: dict={}):
        super().__init__("div", children=[bind], className=className, props=props)
        self.bind = bind
        self.onclick = onClick

    def dom(self):
        el = super().dom()
        el["onclick"] = self.onclick

        return el

