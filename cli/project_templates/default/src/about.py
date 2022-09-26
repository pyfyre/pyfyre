from pyfyre.nodes import *
from text_generator import generate


class AboutPage(Element):
	def __init__(self) -> None:
		super().__init__("div", children=[
			Element("p", children=[TextNode("About Page")]),
			Element("p", children=[TextNode(f"Random string: {generate()}")]),
			Anchor("/", children=[TextNode("Go back")]),
			Element("hr"),
			ListBuilder(lambda index: Element("p", children=[TextNode(index)]))
		])
