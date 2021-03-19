from pynani.core.pynani import Component, RunApp
from pynani.core.widgets import Widgets

widgets = Widgets()

class EndlessContainers(Component):
    def build(self):
        return widgets.container(
            child=widgets.container(
                child=widgets.container(
                    child=widgets.container(
                        child=widgets.container(
                            child=widgets.container(
                                child=widgets.container(
                                    child=widgets.container(
                                        child=widgets.header1(
                                            text="THERE'S NO DEADEND HERE, I CAN GO FAR FROM BEYOND"
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )

RunApp(EndlessContainers())
