# Import PyNani
from pynani.core.pynani import Component, RunApp
from pynani.core.widgets import Widgets

widgets = Widgets()

# Create class called MyApp extends Component from PyNani Core
class MyApp(Component):

    # Where all rendering stuff began in a component...
    def build(self):

        # Returing widgets.container A.K.A <div> in HTML
        # widgets.container(child[Widget], onClick[Javascript], styles[List of CSS Styles])
        return widgets.container(

            # With a child widgets.header1 A.K.A <h1> in HTML
            # widgets.header1(text[String], onClick[Javascript], styles[List of CSS styles])
            child=widgets.header1(
                text="Hello, Jabez!",
                styles=[
                    "margin-top: 10px"
                ]
            )
        )

## To render the widgets into the screen, you need to call RunApp() to compile your code into raw HTML
RunApp(MyApp())
