from pyfyre.widgets import *

class Experiment(Container):
    def __init__(self):
        super().__init__(
            className = "test",
            children = [
                Text(
                    "Try to experiment, edit the `src/main.py` and wait for it to reload automatically on a liveserver. Anyways, I'm a component!",
                    className="desc"
                )
            ]
        )