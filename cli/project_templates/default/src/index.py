from typing import List
from pyfyre import render
from pyfyre.widgets import *
from browser import DOMEvent


class HomePage(StatefulContainer):
	def __init__(self) -> None:
		self.counter = 0
		super().__init__()
	
	def build(self) -> List[BaseWidget]:
		return [
			Widget("h1", children=[TextWidget("Welcome to PyFyre ✨")]),
			Span("This is an example counter app."),
			Paragraph(self.counter),
			Button(self.increment, children=[TextWidget("Count")]),
			HorizontalLine(),
			Link("about", children=[TextWidget("About this website")])
		]
	
	def increment(self, event: DOMEvent) -> None:
		self.counter += 1
		self.update()


class AboutPage(Container):
	def __init__(self) -> None:
		super().__init__(children=[
			Paragraph("About Page")
		])


render("body", {
	"/": HomePage(),
	"/about": AboutPage()
})
