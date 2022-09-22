from typing import List
from pyfyre import render
from pyfyre.widgets import *
from browser import DOMEvent


class App(StatefulContainer):
	def __init__(self) -> None:
		self.counter = 0
		super().__init__(children=[
			Paragraph(self.counter),
			Button(self.increment, children=[TextWidget("Increase")])
		])
	
	def build(self) -> List[BaseWidget]:
		return [
			Paragraph(self.counter),
			Button(self.increment, children=[TextWidget("Increase")])
		]
	
	def increment(self, event: DOMEvent) -> None:
		self.counter += 1
		print(self.counter)
		self.update()


render("body", App())
