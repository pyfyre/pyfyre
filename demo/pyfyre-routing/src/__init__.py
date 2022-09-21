from pyfyre.widgets import *
from pyfyre.pyfyre import runApp

class App(UsesState):
    def __init__(self):
        self.greet = "Welcome"

    def build(self):
        return Router(
            routes={
                "/": Home(),
                "/about": About()
            }
        )

class Home(UsesState):
    def build(self):
        return Container(
            props={"style": "height: 100vh; width: 100vw; display: flex; flex-direction: column; justify-content: center;"},
            children=[
                Text(
                    "Welcome to Home page!",
                    props={"style": "margin-left: auto; margin-right: auto; font-size: 50px;"}
                ),
                Link(
                    "Go to About",
                    to="/about",
                    props={"style": "margin-left: auto; margin-right: auto; font-size: 50px;"}
                )
            ]
        )

class About(UsesState):
    def build(self):
        return Container(
            props={"style": "height: 100vh; width: 100vw; display: flex; flex-direction: column; justify-content: center;"},
            children=[
                Text(
                    "Welcome to About page!",
                    props={"style": "margin-left: auto; margin-right: auto; font-size: 50px;"}
                ),
                Link(
                    "Go home",
                    to="/",
                    props={"style": "margin-left: auto; margin-right: auto; font-size: 50px;"}
                )
            ]
        )

runApp(
    App(),
    mount="app-mount"
)