from pyf_modules.widgets import *
from pyf_modules.pyfyre import runApp

class App(PyFyreApp):
    def __init__(self):
        self.count = 0

    def build(self):
        
        def increment(event):
            self.count = self.count + 1
            self.update()

        def decrement(event):
            self.count = self.count - 1
            self.update()

        return Container(
            className = "container",
            children = [
                Text(
                    className = "title",
                    textContent = "Welcome to PyFyre!"
                ),
                Text(
                    className = "desc",
                    textContent = "Try the Counter app on the bottom and make an experiment, edit the src/main.py and wait for it to reload automatically on a liveserver."
                ),
                Container(
                    className = "counter-app",
                    children = [
                        Button(
                            className="btn",
                            textContent="-",
                            onClick=decrement
                        ),
                        Text(
                            className="counter",
                            textContent=self.count
                        ),
                        Button(
                            className="btn",
                            textContent="+",
                            onClick=increment
                        )
                    ]
                )
            ]
        )
        
runApp(
    App(),
    mount="app-mount"
)