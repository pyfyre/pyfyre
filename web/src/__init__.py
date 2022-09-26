from pyfyre.widgets import *
from pyfyre.pyfyre import runApp
from pyfyre.router import Router
from src.main import HomePage
from src.components.header import Header
from src.playground import PlaygroundPage

from browser import document

class App(UsesState):
    def build(self):
        return Router(
            routes={
                "/": Home(),
                "/playground": Playground()
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

class Playground(Container):
    def __init__(self):
        super().__init__(
            className = "home",
            children = [
                Header(),
                PlaygroundPage()
            ]
        )

runApp(
    App(),
    mount="app-mount"
)