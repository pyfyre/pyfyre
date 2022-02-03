from src.components.counterapp import CounterApp
from pyfyre.widgets import *
from src.components.experiment import Experiment

# You can make components by inherting a Widget class
# and initialize it on the `super().__init__()`.
class MyWebpage(UsesState):
    def __init__(self, greet):
        self.greet = greet

    def build(self):
        return Container(
            className = "container",
            children = [
                Text(
                    f"{self.greet} to PyFyre!",
                    className="title"
                ),
                Experiment(),
                CounterApp()
            ]
        )