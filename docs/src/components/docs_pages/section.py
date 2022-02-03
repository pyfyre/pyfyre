from pyfyre.widgets import *

class Section(Container):
    def __init__(self, title, content):
        super().__init__(
            className="text-base",
            children=[
                Text(
                    className="text-4xl font-bold",
                    textContent=title
                ),
                content()
            ]
        )