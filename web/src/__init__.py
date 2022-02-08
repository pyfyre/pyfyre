from pyfyre.widgets import *
from pyfyre.pyfyre import runApp
from pyfyre.router import Router
from src.main import HomePage
from src.components.header import Header

class App(UsesState):
    def build(self):
        return Router(
            routes={
                "/": Home()
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

runApp(
    App(),
    mount="app-mount"
)