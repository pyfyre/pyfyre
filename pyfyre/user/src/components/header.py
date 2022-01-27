from pyf_modules.widgets import *

class Header(Container):
    def __init__(self):
        super().__init__(
            className = "test",
            children = [
                Text(
                    className = "text",
                    textContent = "Hello there, I'm a header component!"
                )
            ]
        )