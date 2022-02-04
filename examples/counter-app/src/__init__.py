from pyfyre.widgets import *
from pyfyre.pyfyre import runApp

class App(UsesState):
    def __init__(self):
        self.count = 0

    def increment(self, event):
        self.count = self.count + 1
        self.update()

    def decrement(self, event):
        self.count = self.count - 1
        self.update()

    def build(self):
        return Container(
            props={"style": "height: 100vh; width: 100vw; display: flex; flex-direction: column; justify-content: center; align-items: center;"},
            children=[
                Text("Counter app example:"),
                Container(
                    className="counters",
                    children=[
                        Button(
                            "-",
                            onClick=self.decrement,
                            className="btn-counter"
                        ),
                        Text(self.count),
                        Button(
                            "+",
                            onClick=self.increment,
                            className="btn-counter"
                        )
                    ]
                )
            ]
        )
        
runApp(
    App(),
    mount="app-mount"
)