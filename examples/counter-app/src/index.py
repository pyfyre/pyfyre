from pyfyre.nodes import *
from browser import DOMEvent
from pyfyre import render, State


class App(Widget):
	def __init__(self) -> None:
		self.count = State[int](0)
		super().__init__()

	def build(self) -> Element:
		def increment(event: DOMEvent) -> None:
			self.count.set_value(self.count.value + 1)

		def decrement(event: DOMEvent) -> None:
			self.count.set_value(self.count.value - 1)

		return Element("main", lambda: [
			Button(
				onclick=decrement,
				children=lambda: [Text("-")]
			),
			Text(" "),
			Text(self.count),
			Text(" "),
			Button(
				onclick=increment,
				children=lambda: [Text("+")]
			)
		])


render({"/": lambda: App()})
