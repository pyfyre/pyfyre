from pyfyre import render
from pyfyre.nodes import *
from pyfyre import State

class App(Widget):
	def __init__(self):
		self.count = State[int](0)

		super().__init__()

	def build(self) -> Element:

		def increment(e):
			self.count.set_value(self.count.value + 1)

		def decrement(e):
			self.count.set_value(self.count.value - 1)

		return Element("main", lambda: [
			Button(
				onclick=decrement,
				children=lambda: [ Text("-") ]
			),
			Text(self.count),
			Button(
				onclick=increment,
				children=lambda: [ Text("+") ]
			)
		])


render({"/": lambda: App()})
