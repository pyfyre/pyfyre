from pyfyre.widgets.widget import Widget

class UIBaseException:
    def __init__(self, msg, e):
        self.msg = msg
        self.e = e

    def dom(self):
        print(f"Uncaught exception: {self.e}")

        return self.TextException(self.msg).dom()

    class TextException(Widget):
        def __init__(self, msg: str, attrs: dict=None):
            super().__init__("h1", children=msg, attrs=attrs)

class RenderError(UIBaseException): ...
class InvalidController(BaseException): ...