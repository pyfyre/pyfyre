from pynani.core.pynani import Component, RunApp
from pynani.core.widgets import Widgets

widgets = Widgets()

class MyApp(Component):
    def build(self):
        return widgets.header1(
            text="Hello, World!",
            styles=[
                "margin: 30px"
            ]
        )

RunApp(MyApp())