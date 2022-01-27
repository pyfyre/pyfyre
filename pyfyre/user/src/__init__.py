from pyf_modules.widgets import *
from src.main import MyWebpage
from src.components.header import Header

# This class is called at `runApp` method
# at the bottom. A class that inherits
# PyFyreApp class has a `build` method that
# should return a Widget.
class App(PyFyreApp):
    def __init__(self):
        # If you want to store a variable, you should store it
        # in `self` at the `__init__` method.
        self.greet = "Hello, there"

    def build(self):

        # You can do some Pythonic things inside
        # the build method.

        return Container(
            className = "root",
            children = [
                Header(self.greet),
                MyWebpage()
            ]
        )

# This is the main entry point of your app.
# Any class that inherits the PyFyreApp class
# should be passed as the first parameter.
# The second parameter is the `mount`, it's
# an provided element id where your app will render.
# Try to take a look at `index.html` and you'll see
# a Div element with an id of `app-mount`.
runApp(
    App(),
    mount="app-mount"
)