from pyf_modules.widgets import *
from src.main import MyWebpage
from src.components.header import Header

class App(PyFyreApp):
    def build(self):
        return Container(
            className = "root",
            children = [
                Header(),
                MyWebpage()
            ]
        )

runApp(
    App(),
    mount="app-mount"
)