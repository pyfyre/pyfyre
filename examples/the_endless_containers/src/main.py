from pynani.core.pynani import Component, RunApp
from pynani.core.widgets import Widgets

widgets = Widgets()

class MyApp(Component):
    def build(self):
        return utils.container(
            child=utils.container(
                child=utils.container(
                    child=utils.header1(
                        text="HAHA I AM AT THE SUPER INSIDE OF A DIV :)"
                    )
                )
            )
        )

RunApp(MyApp())