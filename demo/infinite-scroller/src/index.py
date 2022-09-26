from pyfyre import render
from pyfyre.nodes import *


class App(Element):
	def __init__(self) -> None:
		super().__init__("main", children=[
			Element("h1", children=[TextNode("Infinite Scroller")]),
			ListBuilder(lambda index: Element("p", children=[TextNode(index)]))
		])


render("body", {"/": App()})
