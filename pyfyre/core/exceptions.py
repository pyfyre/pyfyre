from pyfyre.widgets.widget import Widget

class BaseException:
    def __init__(self, e):
        self.e = e

    def dom(self):
        return self.TextException(self.e).dom()

    class TextException(Widget):
        def __init__(self, error: str, className="", props: dict=None):
            super().__init__("h1", className=className, props=props)
            self.error = error
        
        def dom(self):
            element = super().dom()
            element.textContent = self.error
            
            element.attrs["style"] = "background-color: #efa3a3; width: fit-content; padding: 10px;"
            
            return element

class RenderError(BaseException):
    pass