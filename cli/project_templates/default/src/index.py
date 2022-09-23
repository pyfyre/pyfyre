from typing import List
from pyfyre import render
from about import AboutPage
from pyfyre.widgets import *
from browser import DOMEvent


class HomePage(Container):
	def __init__(self) -> None:
		super().__init__(children=[
			Widget("h1", children=[TextWidget("Welcome to PyFyre ✨")]),
			Span("This is an example counter app."),
			Counter(),
			HorizontalLine(),
			InternalLink("about", children=[TextWidget("About this website")])
		])


class Counter(StatefulContainer):
	def __init__(self) -> None:
		self.counter = 0
		super().__init__()
	
	def build(self) -> List[BaseWidget]:
		if self.counter == 3:
			raise Exception("Intentional raise condition when count is 3")
		
		return [
			Paragraph(self.counter),
			Button(self.increment, children=[TextWidget("Count")])
		]
	
	def on_build_error(
		self, exc_type, exc_value, exc_traceback
	) -> List[BaseWidget]:
		return [
			Paragraph(exc_value),
			Button(self.increment, children=[TextWidget("Count")])
		]
	
	def increment(self, event: DOMEvent) -> None:
		self.counter += 1
		self.update()


render("body", {
	"/": HomePage(),
	"/about": AboutPage()
})
