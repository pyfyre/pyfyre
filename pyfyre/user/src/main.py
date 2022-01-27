from pyf_modules.widgets import *

class MyWebpage(Container):
    def __init__(self):
        super().__init__(
            className = "container",
            children = [
                Text(
                    className = "title",
                    textContent = "Welcome to PyFyre!"
                ),
                Text(
                    className = "desc",
                    textContent = "Try to experiment, edit the `src/main.py` and wait for it to reload automatically on a liveserver."
                )
            ]
        )