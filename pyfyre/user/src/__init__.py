from pyfyre.widgets import *
from pyfyre.pyfyre import runApp
from src.main import MyWebpage

# This class is called at `runApp` method
# at the bottom. A class that inherits
# UsesState class has a `build` method that
# should return a Widget.
class App(UsesState):
    def __init__(self):
        # If you want to store a variable, you should store it
        # in `self` at the `__init__` method.
        self.greet = "Welcome"

    def build(self):

        # You can do some Pythonic things inside
        # the build method.

        return MyWebpage(self.greet)

# This is the main entry point of your app.
# Any class that inherits the UsesState class
# should be passed as the first parameter.
# The second parameter is the `mount`, it's
# an provided element id where your app will render.
# Try to take a look at `index.html` and you'll see
# a Div element with an id of `app-mount`.
runApp(
    App(),
    mount="app-mount"
)