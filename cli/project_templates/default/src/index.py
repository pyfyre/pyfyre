from pyfyre import render
from pyfyre.widgets import Widget, TextWidget


class App(Widget):
	def __init__(self) -> None:
		super().__init__(
			"h1",
			children=[TextWidget("Welcome to PyFyre ✨")]
		)


render("body", App())
