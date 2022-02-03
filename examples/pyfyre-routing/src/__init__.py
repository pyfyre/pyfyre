from pyf_modules.widgets import *
from pyf_modules.pyfyre import runApp

class App(UsesState):
    def build(self):
        return Container(
            className = "container",
            children = [
                Text(
                    className="text",
                    textContent="Go to another page"
                ),
                Link(
                    className="link",
                    textContent="About",
                    page=AboutPage
                ),
            ]
        )

class AboutPage(UsesState):
    def build(self):
        return Container(
            className="container-2",
            children=[
                Text(
                    className="text-2",
                    textContent="ABOUT PAGE"
                ),
                Link(
                    className="link",
                    textContent="Home",
                    page=App
                )
            ]
        )
        
runApp(
    App(),
    mount="app-mount"
)