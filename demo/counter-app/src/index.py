from pyfyre import render
from pyfyre.nodes import *
from browser import DOMEvent


class App(Element):
	def __init__(self) -> None:
		self.count = 0
		self.text = TextNode(self.count)
		
		super().__init__("main", children=[
			Element("h1", children=[TextNode("Counter App")]),
			Element("p", children=[self.text]),
			Button(self.decrement, children=[TextNode("-")]),
			Button(self.increment, children=[TextNode("+")])
		])
	
	def increment(self, event: DOMEvent) -> None:
		self.count += 1
		self.text.set_value(self.count)
		self.text.update_dom()
	
	def decrement(self, event: DOMEvent) -> None:
		self.count -= 1
		self.text.set_value(self.count)
		self.text.update_dom()


render("body", {"/": App()})
