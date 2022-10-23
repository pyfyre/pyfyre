from pyfyre.nodes import *
from browser import DOMEvent
from pyfyre import render, State


class App(Widget):
	def __init__(self) -> None:
		# A State object with a list of strings and default value of ["Hello"]
		self.todos = State[list[str]](["Hello"])

		# TextInput is declared as variable to get the value of it in the Widget.
		self.text_input = TextInput()

		super().__init__()

	def build(self) -> Element:
		def todo(index: int) -> Element:
			# Wrapped in Element("p") to add block display styling
			return Element("p", children=lambda: [Text(self.todos.value[index])])

		def add_todo(event: DOMEvent) -> None:
			if self.text_input.value:
				self.todos.set_value(self.todos.value + [self.text_input.value])

		return Element("main", lambda: [
			Element(
				"div",
				children=lambda: [
					ListBuilder(
						children_builder=todo,
						count=len(self.todos.value)
					),
				],
				# Element("div") will be automatically rerendered once its
				# dependency states has been updated.
				states=[self.todos]
			),
			self.text_input,
			Button(onclick=add_todo, children=lambda: [Text("Add Todo")])
		])


render({"/": lambda: App()})
