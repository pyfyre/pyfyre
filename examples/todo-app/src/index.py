from pyfyre import render
from pyfyre.nodes import *
from pyfyre import State

class App(Widget):
	def __init__(self):
		self.todos = State[list[str]](["Hello"]) # A State object with a list of strings and default value of ["Hello"]

		self.text_input = TextInput() # TextInput is declared as variable to get the value of it in the Widget.

		super().__init__()

	def build(self) -> Element:

		def todo(i):
			return Element("p", children=lambda: [ Text(self.todos.value[i]) ]) # Wrapped in Element("p") to remove inline-block

		def add_todo(e):
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
				states=[self.todos] # Element("div") will be automatically rerendered once its dependency states has been updated.
			),
			self.text_input,
			Button(onclick=add_todo, children=lambda: [ Text("Add Todo") ])
		])


render({"/": lambda: App()})
