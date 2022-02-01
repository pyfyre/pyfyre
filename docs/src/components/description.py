from pyfyre.widgets import *

class Descriptions(Container):
    def __init__(self):
        super().__init__(
            className="",
            children=[
                Image(),
                Container(
                    children=[
                        Text(),
                        Text(),
                        Text()
                    ]
                )
            ]
        )