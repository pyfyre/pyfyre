from pyfyre import render
from pyfyre.nodes import *
from browser import DOMEvent
from text_generator import generate


class App(Element):
	def __init__(self) -> None:
		self.text = TextNode(generate() or "Try again.")
		
		super().__init__("main", lambda: [
			Element("h1", lambda: [TextNode("Random String Generator")]),
			Element("p", lambda: [self.text]),
			Button(self.generate, lambda: [TextNode("Generate")])
		])
	
	def generate(self, event: DOMEvent) -> None:
		self.text.set_value(generate() or "Try again.")
		self.text.update_dom()


render("body", {"/": lambda: App()})
