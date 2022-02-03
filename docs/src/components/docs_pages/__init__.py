from pyfyre.widgets import *

class DocsPage(Container):
    def __init__(self, content):
        super().__init__(
            className="text-[#222222] px-52 py-10 ml-52",
            children=[
                content()
            ]
        )