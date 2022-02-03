from pyfyre.widgets import *
from pyfyre.pyfyre import runApp
from src.main import HomePage
from src.components.header import Header
from src.components.docs import Docs

class App(UsesState):
    def __init__(self):
        self.greet = "Hello, there"

    def build(self):
        return Router(
            routes={
                "/": Home(),
                "/?": Documentation(),
                "/docs": Documentation(),
                "/docs/introduction": Documentation(),
                "/docs/installation": Documentation(),
            }
        )
        
class Home(Container):
    def __init__(self):
        super().__init__(
            className = "home",
            children = [
                Header(),
                HomePage()
            ]
        )

class Documentation(Container):
    def __init__(self):
        super().__init__(
            className="docs",
            children=[
                Header(),
                Docs()
            ]
        )

runApp(
    App(),
    mount="app-mount"
)