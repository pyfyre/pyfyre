from pyfyre import render
from pyfyre.nodes import *


class App(Element):
	def __init__(self) -> None:
		super().__init__("main", lambda: [
			Element("h1", lambda: [TextNode("Infinite Scroller")]),
			ListBuilder(lambda index: Element("p", lambda: [TextNode(index)]))
		])


render("body", {"/": lambda: App()})
