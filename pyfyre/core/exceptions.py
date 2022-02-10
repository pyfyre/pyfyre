from pyfyre.widgets.widget import Widget

class UIBaseException:
    def __init__(self, msg, e):
        self.msg = msg
        self.e = e

    def dom(self):
        print(f"Uncaught exception: {self.e}")

        return self.TextException(self.msg).dom()

    class TextException(Widget):
        def __init__(self, msg: str, className="", props: dict=None):
            super().__init__("h1", className=className, props=props)
            self.msg = msg
        
        def dom(self):
            element = super().dom()
            element.textContent = self.msg
            
            element.attrs["style"] = "background-color: #efa3a3; width: fit-content; padding: 10px;"
            
            return element

class RenderError(UIBaseException): ...
class InvalidController(BaseException): ...