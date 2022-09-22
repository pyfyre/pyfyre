from typing import List
from pyfyre import render
from pyfyre.widgets import *
from browser import DOMEvent


class App(StatefulContainer):
	def __init__(self) -> None:
		self.counter = 0
		super().__init__()
	
	def build(self) -> List[BaseWidget]:
		return [
			Widget("h1", children=[TextWidget("Welcome to PyFyre ✨")]),
			Span("This is an example counter app."),
			Paragraph(self.counter),
			Button(self.increment, children=[TextWidget("Count")])
		]
	
	def increment(self, event: DOMEvent) -> None:
		self.counter += 1
		self.update()


render("body", App())
