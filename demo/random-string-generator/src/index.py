from pyfyre import render
from pyfyre.nodes import *
from browser import DOMEvent
from text_generator import generate


class App(Element):
	def __init__(self) -> None:
		self.text = TextNode(generate() or "Try again.")
		
		super().__init__("main", children=[
			Element("h1", children=[TextNode("Random String Generator")]),
			Element("p", children=[self.text]),
			Button(self.generate, children=[TextNode("Generate")])
		])
	
	def generate(self, event: DOMEvent) -> None:
		self.text.set_value(generate() or "Try again.")
		self.text.update_dom()


render("body", {"/": App()})
