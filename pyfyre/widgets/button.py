from pyfyre.widgets.widget import Widget

class Button(Widget):
    """Creates a Button widget.

    Attributes
    ----------
    textContent : str (positional)
        The text content of the button.
    onClick : method
        The method you provided where when the button has been clicked
        or activate, the [onClick] method will be fired automatically.
    """
    
    def __init__(self, textContent, className="", onClick=lambda: print(""), props: dict={}):
        super().__init__("button", children=textContent, className=className, props=props)
        self.textContent = textContent
        self.onClick = onClick

    def dom(self):
        el = super().dom()
        el["onclick"] = self.onClick

        return el