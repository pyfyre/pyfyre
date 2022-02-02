from pyfyre.widgets import *
from src.components.experiment import Experiment

# You can make components by inherting a Widget class
# and initialize it on the `super().__init__()`.
class MyWebpage(Container):
    def __init__(self, greet):
        super().__init__(
            className = "container",
            children = [
                Text(
                    f"{greet} to PyFyre!",
                    className="title"
                ),
                Experiment()
            ]
        )